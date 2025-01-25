# ---- Environment and Variable Setup ---- #
import os
from dotenv import load_dotenv
from openai import OpenAI
import time
from tqdm import tqdm
import re
import pandas as pd
import numpy as np
from requests.exceptions import HTTPError
from rubrics_with_few_shot_examples import RubricsWithFewShotExamples
from pathlib import Path
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure paths
BASE_DIR = Path('repository/data/raw')
API_KEY_PATH = BASE_DIR.parent.parent / 'scripts/OPENAI-API-KEY.env'

# Add dataset configuration
class DatasetConfig:
    def __init__(self, essay_set_num, model_name):
        self.essay_set_num = essay_set_num
        self.output_dir = BASE_DIR.parent / 'processed' / f'Essay_Set_#{essay_set_num}'
        self.sample_data_path = BASE_DIR / f'Essay_Set_#{essay_set_num} - 副本.xlsx'
        
        # Model to index mapping
        model_index_map = {
            'gpt-4o-mini-2024-07-18': 1,
            'gpt-4o-2024-08-06': 2,
            'claude-3-5-haiku-20241022': 3,
            'claude-3-5-sonnet-20241022': 4
        }
        
        # Get model index
        model_index = model_index_map.get(model_name, 1)  # Default to 1 if model name not found
        
        # Set output file paths
        self.machine_rater_data_path = self.output_dir / f'machine_rater_data_{essay_set_num}_{model_index}.csv'
        self.complement_output_path = self.output_dir / f'machine_rater_data_{essay_set_num}_{model_index}_1.csv'

def get_rubrics_and_prompt(rubrics, essay_set_num):
    """Get corresponding rubrics and prompts based on essay set number"""
    rubrics_map = {
        1: (rubrics.Set_1_Rubric, rubrics.Set_1_Prompt, rubrics.Set_1_Task_Decomposition),
        2: (rubrics.Set_2_Rubric, rubrics.Set_2_Prompt, rubrics.Set_2_Task_Decomposition),
        3: (rubrics.Set_3_Rubric, rubrics.Set_3_Prompt, rubrics.Set_3_Task_Decomposition)
    }
    return rubrics_map.get(essay_set_num)

# Load environment variables
load_dotenv(API_KEY_PATH, override=True)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url='https://api.openai.com/v1')

# Custom exception class
class APICallError(Exception):
    pass

# Improved API call function
def call_writing_assessment(rubrics, essay, model, essay_set_num, max_retries=3, retry_delay=7):
    for attempt in range(max_retries):
        try:
            logging.info(f"Attempting API call for Essay Set #{essay_set_num}, attempt {attempt + 1}")
            # Get corresponding rubrics and prompt based on essay set number
            rubric, prompt, task_decomposition = get_rubrics_and_prompt(rubrics, essay_set_num)
            
            return writing_assessment(
                rubric,
                prompt,
                essay,
                task_decomposition,
                model
            )
        except HTTPError as http_err:
            logging.error(f"HTTP Error: {http_err}")
            if http_err.response.status_code == 400:
                return "Sensitive word detecting"
            elif http_err.response.status_code == 503:
                return "No available model"
            elif attempt == max_retries - 1:
                raise APICallError(f"Maximum retries reached: {http_err}")
            logging.warning(f"Attempt {attempt + 1} failed: {http_err}")
            time.sleep(retry_delay * (attempt + 1))
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            raise
    return None

# Extract score from response text
def extract_score(text):
    match = re.findall(r'(\d+)', text)
    return int(match[-1]) if match else -1

def extract_score_set1_2(text):
    """
    Extract final score or overall score from the given evaluation text (for datasets 1 and 2)
    
    Supported formats:
    - Final Score: 3
    - Overall Score: 4
    - Score Point: 2
    - **Final Score:** 1
    - **Score:** 2
    - **Final Score: 4.5 (Rounded to 5)**
    - rounded to 4
    - Overall Holistic Score: 3
    - **Final Holistic Score: 3**
    - Score Point 2
    - Score: 2
    - **Score 3**
    
    When multiple scores are found, the last one will be used.
    Returns:
        float: Extracted score, or -1 if no score found
    """
    text_clean = re.sub(r'\*+', '', text or '').strip()

    patterns = [
        # If "rounded to X" is detected, return X directly
        r'[Rr]ounded to\s*(\d+)',
        
        # Version with parentheses (e.g., Final Score: 4.5 (Rounded to 5))
        r'(?:Final|Overall|Holistic)?\s*Score\s*:?[\s-]*(\d+(?:\.\d+))\s*\(Rounded to \d+\)',
        
        # Common formats: "Final Score: X", "Overall Score: X", "Score Point X", "Holistic Score X"
        r'(?:Final Score|Overall Score|Score Point|Holistic Score)\s*[:\-]?\s*(\d+(?:\.\d+)?)',
        
        # "Score : X" or "Score X"
        r'Score\s*[:\-]?\s*(\d+(?:\.\d+)?)'
    ]

    last_valid_score = -1
    
    for pattern in patterns:
        # Find all matches for the current pattern
        matches = list(re.finditer(pattern, text_clean, re.IGNORECASE))
        if matches:
            # Try to extract score from the last match
            try:
                last_match = matches[-1]
                score_str = last_match.group(1)
                last_valid_score = float(score_str)
            except (ValueError, IndexError):
                continue
    
    return last_valid_score

def extract_score_set3(text):
    """
    Extract scores for six dimensions from the given evaluation text (for dataset 3)
    
    Dimensions:
    - Ideas and Content Score
    - Organization Score
    - Voice Score
    - Word Choice Score
    - Sentence Fluency Score
    - Convention Score
    
    When multiple scores are found for a dimension, the last one will be used.
    Returns:
        list: List of six scores, -1 for any dimension where score not found
    """
    text_clean = re.sub(r'\*+', '', text or '').strip()
    
    patterns = [
        r'Ideas and Content Score\s*[:\-]\s*(\d+(?:\.\d+)?)',
        r'Organization Score\s*[:\-]\s*(\d+(?:\.\d+)?)',
        r'Voice Score\s*[:\-]\s*(\d+(?:\.\d+)?)',
        r'Word Choice Score\s*[:\-]\s*(\d+(?:\.\d+)?)',
        r'Sentence Fluency Score\s*[:\-]\s*(\d+(?:\.\d+)?)',
        r'Convention Score\s*[:\-]\s*(\d+(?:\.\d+)?)'
    ]
    
    scores = []
    for pattern in patterns:
        # Find all matches for the current dimension
        matches = list(re.finditer(pattern, text_clean, re.IGNORECASE))
        if matches:
            try:
                # Use the last match for this dimension
                last_match = matches[-1]
                scores.append(float(last_match.group(1)))
            except (ValueError, IndexError):
                scores.append(-1)
        else:
            scores.append(-1)
    
    return scores

# Improved parallel processing function
def process_sample(i, essay, rubrics, model, essay_set_num, num_evaluations=2):
    scores = []
    evaluations = []
    for _ in range(num_evaluations):
        text = call_writing_assessment(rubrics, essay, model, essay_set_num)
        if text:
            if essay_set_num in [1, 2]:
                score = extract_score_set1_2(text)
                if score != -1:
                    scores.append(score)
                    evaluations.append(text)
            else:  # essay_set_num == 3
                score_dict = extract_score_set3(text)
                if not all(v == -1 for v in score_dict.values()):
                    scores.append(score_dict)
                    evaluations.append(text)
    return i, scores, evaluations

# Add batch processing functionality
def process_in_batches(sample_data, batch_size=10):
    for i in range(0, len(sample_data), batch_size):
        yield sample_data[i:i + batch_size]

# Assessment function
def writing_assessment(rubrics, prompt, essay, task_decomposition, model):
    completion = client.chat.completions.create(
        model=model,
        max_tokens=2024,
        messages=[
            {"role": "system", "content": """As a virtual evaluator with expertise in English composition, your role is to critically analyze and grade student essays according to a predetermined set of rubrics. You are to act as an impartial judge and evaluate the essays based on the quality of the writing and adherence to the essay prompt."""},
            {"role": "user", "content": f"""
                Here are the specific guidelines for each score:
                ```
                {rubrics}
                ```
                \n Sample Essay Prompt:
                ```
                {prompt}
                ```
                \n Student's Essay to Evaluate:
                ```
                {essay}   
                ```
                \n All the essays are anonymized. This means that named entities (people, places, dates, times, organizations, etc.) are replaced with placeholders (Eg. @NAME1, @LOCATION1, etc.). In addition to this, capitalized phrases are anonymized as @CAP1, @CAP2, etc.
                \n These anonymizations SHOULD NOT affect your scoring. You are free to replace the anonymizations with any placeholders.
                \n Task Breakdown:
                ```
                {task_decomposition}
                ```
            """}
        ],
        temperature=0
    )
    return completion.choices[0].message.content

# Main scoring function (parallel)
def machine_scoring_main_parallel(sample_data, rubrics, model, essay_set_num, max_workers=2):
    person_list = [None] * len(sample_data)
    evaluation_list = [None] * len(sample_data)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(process_sample, i, sample_data['essay'][i], rubrics, model, essay_set_num): i
            for i in range(len(sample_data))
        }
        for future in tqdm(as_completed(futures), total=len(futures), desc='Processing samples'):
            i, scores, evaluations = future.result()
            if len(scores) == 2:
                person_list[i] = scores
                evaluation_list[i] = evaluations
    return person_list, evaluation_list

# Complementary scoring function (parallel)
def machine_scoring_complement_parallel(sample_data, indices, person_list, evaluation_list, rubrics, model, max_workers=2):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(process_sample, i, sample_data['essay'][i], rubrics, model): i
            for i in indices
        }
        for future in tqdm(as_completed(futures), total=len(futures), desc='Completing samples'):
            i, scores, evaluations = future.result()
            if len(scores) == 2:
                person_list[i] = scores
                evaluation_list[i] = evaluations
    return person_list, evaluation_list

def validate_data_columns(df, required_columns=['Essay_id', 'essay']):
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
        
# Main program
def main(essay_set_num=2, model_name='gpt-4o-2024-08-06'):
    config = DatasetConfig(essay_set_num, model_name)
    
    # Create output directory if it doesn't exist
    config.output_dir.mkdir(parents=True, exist_ok=True)
    
    sample_data = pd.read_excel(config.sample_data_path)
    validate_data_columns(sample_data)  # 验证数据列
    print("Available columns:", sample_data.columns.tolist())
    logging.info(f"Loaded {len(sample_data)} samples from Essay Set #{essay_set_num}")
    
    rubrics = RubricsWithFewShotExamples()
    rubric, prompt, task_decomposition = get_rubrics_and_prompt(rubrics, essay_set_num)
    model = model_name  # Use the provided model name
    Demands = 'Building Method'  # Options: 'Building Method'/'Complementing Method'

    if Demands == 'Building Method':
        person_list, evaluation_list = machine_scoring_main_parallel(sample_data, rubrics, model, essay_set_num)
        
        Person = sample_data['Essay_id'].to_numpy()
        Persons = np.repeat(Person, 2)
        Rater_Type = np.repeat(2, len(person_list) * 2)
        Raters = np.tile(np.arange(3, 5), len(person_list))
        
        # Create base DataFrame
        machine_rater_data = pd.DataFrame({
            'Essay_id': Persons,
            'Rater_Type': Rater_Type,
            'Raters': Raters,
            'Evaluations': np.array(evaluation_list).flatten()
        })
        
        # Extract scores based on dataset type
        if essay_set_num in [1, 2]:
            machine_rater_data['Scores'] = machine_rater_data['Evaluations'].apply(extract_score_set1_2)
        else:
            # Extract scores for six dimensions
            scores = machine_rater_data['Evaluations'].apply(extract_score_set3)
            score_columns = ['Ideas_Content', 'Organization', 'Voice', 
                           'Word_Choice', 'Sentence_Fluency', 'Convention']
            for i, col in enumerate(score_columns):
                machine_rater_data[col] = scores.apply(lambda x: x[i])
        
        # Sort and save
        machine_rater_data = machine_rater_data.sort_values(['Essay_id', 'Raters'])
        machine_rater_data.to_csv(config.machine_rater_data_path, index=False)
        
    elif Demands == 'Complementing Method':
        machine_rater_data = pd.read_csv(config.machine_rater_data_path, encoding='iso-8859-1')
        specific_value = -1
        selected_essay_id = machine_rater_data.loc[machine_rater_data['Scores'] == specific_value, 'Essay_id']
        unqualified_indices = sample_data[sample_data['Essay_id'].isin(selected_essay_id)].index.tolist()
        
        # Only score unqualified samples
        person_list = [None] * len(unqualified_indices)
        evaluation_list = [None] * len(unqualified_indices)
        
        # Score unqualified samples
        for i, idx in enumerate(tqdm(unqualified_indices, desc='Processing samples')):
            try:
                scores = []
                evaluations = []
                for _ in range(2):  # Each sample needs 2 scores
                    text = writing_assessment(rubrics.Set_1_Rubric, rubrics.Set_1_Prompt, 
                                        sample_data['essay'][idx], rubrics.Set_1_Task_Decomposition, model)
                    evaluations.append(text)
                    # Extract score
                    match = re.findall(r'(\d+)', text)
                    scores.append(int(match[-1]) if match else -1)
                person_list[i] = scores
                evaluation_list[i] = evaluations
            except Exception as e:
                print(f"Error processing sample {idx}: {e}")
                person_list[i] = [-1, -1]
                evaluation_list[i] = ['Error', 'Error']
                
        # Update scores in dataframe
        for i, idx in enumerate(unqualified_indices):
            if essay_set_num in [1, 2]:
                machine_rater_data.loc[idx * 2, 'Scores'] = extract_score_set1_2(evaluation_list[i][0])
                machine_rater_data.loc[idx * 2 + 1, 'Scores'] = extract_score_set1_2(evaluation_list[i][1])
            else:
                scores1 = extract_score_set3(evaluation_list[i][0])
                scores2 = extract_score_set3(evaluation_list[i][1])
                score_columns = ['Ideas_Content', 'Organization', 'Voice', 
                               'Word_Choice', 'Sentence_Fluency', 'Convention']
                for j, col in enumerate(score_columns):
                    machine_rater_data.loc[idx * 2, col] = scores1[j]
                    machine_rater_data.loc[idx * 2 + 1, col] = scores2[j]
            
            machine_rater_data.loc[idx * 2, 'Evaluations'] = evaluation_list[i][0]
            machine_rater_data.loc[idx * 2 + 1, 'Evaluations'] = evaluation_list[i][1]
        
        # Save updated results
        machine_rater_data.to_csv(config.complement_output_path, index=False)

if __name__ == "__main__":
    essay_set_num = 2
    model_name = 'gpt-4o-2024-08-06'
    logging.info(f"Processing Essay Set #{essay_set_num} with model {model_name}")
    main(essay_set_num, model_name)