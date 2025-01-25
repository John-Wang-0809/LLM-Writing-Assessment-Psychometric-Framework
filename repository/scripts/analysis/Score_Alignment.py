import pandas as pd
import re
import os

def extract_score_set1_2(text):
    """
    Extract final score or overall score from the given evaluation text (for datasets 1 and 2)
    
    First finds "your final evaluation" or "final evaluation" (case insensitive),
    then looks for scores within 50 characters after these phrases.
    If not found, looks for scores in the entire text.
    Few lines need to be checked manually.
    
    Returns:
        float: Extracted score, or -1 if no score found
    """
    if not text:
        return -1
        
    text_clean = re.sub(r'\*+', '', text).strip()
    
    # Find evaluation marker words
    eval_pattern = r'(?:your\s+)?final\s+evaluation'
    eval_matches = list(re.finditer(eval_pattern, text_clean, re.IGNORECASE))
    
    patterns = [
        # "Score : X" or "Score X" or "Score: X"
        r'Score\s*[::\-]?\s*(\d+(?:\.\d+)?)',

        # "Final Score: X"
        r'Final Score:\s*(\d+(?:\.\d+)?)',

        # Version with parentheses (e.g., Final Score: 4.5 (Rounded to 5))
        r'(?:Final|Overall|Holistic)?\s*Score\s*:?[\s-]*(\d+(?:\.\d+))\s*\(Rounded to \d+\)',
        
        # Common formats: "Final Score: X", "Overall Score: X", "Score Point X", "Holistic Score X"
        r'(?:Overall Score|Score Point|Holistic Score|Final Score)\s*[:\-]?\s*(\d+(?:\.\d+)?)',
        
        # If "rounded to X" is detected, return X directly
        r'[Rr]ounded to\s*(\d+)',

        # Match "Leaning towards X" or "Leaning towards a X"
        r'[Ll]eaning towards(?:\s+a)?\s*(\d+(?:\.\d+)?)'
    ]

    if eval_matches:
        # Get position of last evaluation marker
        last_eval_end = eval_matches[-1].end()
        # Search for score within 50 characters after evaluation marker
        search_text = text_clean[last_eval_end:last_eval_end+2500]
    else:
        # If no evaluation marker found, search entire text
        search_text = text_clean

    for pattern in patterns:
        matches = list(re.finditer(pattern, search_text, re.IGNORECASE))
        if matches:
            try:
                last_match = matches[-1]
                score_str = last_match.group(1)
                return float(score_str)
            except (ValueError, IndexError):
                continue
    
    return -1

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

def process_csv(input_csv, output_csv, essay_set_num):
    """
    Process CSV file and extract scores based on dataset number.
    
    Args:
        input_csv (str): Path to input CSV file
        output_csv (str): Path to output CSV file
        essay_set_num (int): Dataset number (1, 2, or 3)
    """
    try:
        df = pd.read_csv(input_csv, encoding='iso-8859-1')
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if 'Evaluations' not in df.columns:
        print("'Evaluations' column not found in CSV file")
        return

    if essay_set_num in [1, 2]:
        # For datasets 1 and 2: add single Score column
        df['Score'] = df['Evaluations'].apply(extract_score_set1_2)
    else:
        # For dataset 3: extract six dimension scores
        scores = df['Evaluations'].apply(extract_score_set3)
        score_columns = ['Ideas_Content', 'Organization', 'Voice', 
                        'Word_Choice', 'Sentence_Fluency', 'Convention']
        for i, col in enumerate(score_columns):
            df[col] = scores.apply(lambda x: x[i])

    try:
        df.to_csv(output_csv, index=False)
        print(f"Processing complete. Results saved to {output_csv}")
        
        # Print statistics
        if essay_set_num in [1, 2]:
            print("\nScore extraction statistics:")
            print(f"Total rows: {len(df)}")
            print(f"Successfully extracted scores: {sum(df['Score'] != -1)}")
            print(f"Failed extractions: {sum(df['Score'] == -1)}")
        else:
            print("\nDimension score extraction statistics:")
            for col in score_columns:
                print(f"\n{col}:")
                print(f"Total rows: {len(df)}")
                print(f"Successfully extracted scores: {sum(df[col] != -1)}")
                print(f"Failed extractions: {sum(df[col] == -1)}")
        
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    # Base path
    base_path = "repository/data/processed"
    
    # Model list
    models = [
        'gpt-4o-mini-2024-07-18',  # index 1
        'gpt-4o-2024-08-06',       # index 2
        'claude-3-5-haiku-20241022',  # index 3
        'claude-3-5-sonnet-20241022'  # index 4
    ]
    
    # Process all datasets and models
    for essay_set_num in [1]:
        for model_idx, model_name in enumerate(models, 1):
            print(f"\nProcessing dataset {essay_set_num}, model {model_name}")
            
            # Build input/output paths
            input_csv = os.path.join(base_path, f"Essay_Set_#{essay_set_num}", 
                                   f"machine_rater_data_{essay_set_num}_{model_idx}.csv")
            output_csv = os.path.join(base_path, f"Essay_Set_#{essay_set_num}", 
                                    f"machine_rater_data_{essay_set_num}_{model_idx}_aligned.csv")
            
            # Check if input file exists
            if os.path.exists(input_csv):
                process_csv(input_csv, output_csv, essay_set_num)
            else:
                print(f"File not found: {input_csv}")