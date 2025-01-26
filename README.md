# LLM-Writing-Assessment-Psychometric-Framwork
A repository for evaluating large language models as raters in large-scale writing assessments, focusing on a psychometric framework for reliability and validity.
# Evaluating Large Language Models as Raters in Large-Scale Writing Assessments
**A Psychometric Framework for Reliability and Validity**

This project explores the use of Large Language Models (LLMs) as raters in large-scale writing assessments. Utilizing a psychometric framework, it systematically evaluates the reliability and validity of LLMs compared to human raters. The findings provide new insights and empirical evidence for the Automated Essay Scoring (AES) field, laying the groundwork for optimizing LLM applications in subjective assessment tasks.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Key Findings](#key-findings)
3. [Project Structure](#project-structure)
4. [Installation and Usage](#installation-and-usage)
5. [Citations and References](#citations-and-references)
6. [License](#license)
7. [Contributing](#contributing)
8. [Contact](#contact)

---

## Introduction  
- **Importance of Language Proficiency Tests**: Large-scale international language proficiency tests play a critical role in university admissions, employment opportunities, and immigration processes. Writing tests, in particular, provide deep insights into an examinee’s pragmatic competence.  
  
- **Challenges in Human Scoring**: Assessing writing proficiency is inherently complex. Human raters may suffer from fatigue, personal biases, and cultural differences, leading to inconsistent and subjective evaluations that undermine the assessment's effectiveness.  
  
- **Advancements in Automated Essay Scoring (AES)**: To address these challenges, researchers have developed AES systems leveraging machine intelligence. These systems have evolved from feature-engineered machine learning models to advanced deep learning techniques, including transformer-based models like LLMs, which significantly enhance AES capabilities.  
  
- **Need for Robust Evaluation Metrics**: Current AES evaluations primarily use metrics like Quadratic Weighted Kappa (QWK) to measure score consistency between models and human raters. However, this raises concerns about whether human scoring accurately reflects examinees’ abilities, especially with complex scoring rubrics that can be interpreted variably and subject to biases.  
  
- **Psychometric Framework**: This project employs a psychometric framework, focusing on reliability and validity, to evaluate LLMs as essay evaluators. It leverages Generalizability (G-) Theory and the Many-Facet Rasch Model (MFRM) to provide a comprehensive assessment of both human and model raters.  

---  

## Key Findings  
1. **Reliability**  
   - **Inter-Rater Reliability**: LLMs, particularly Claude, demonstrated higher inter-rater reliability compared to human raters and GPT, especially with complex rating scales.  
   - **Intra-Rater Reliability**: Claude also outperformed GPT in maintaining consistent evaluations over time.  

2. **Validity**  
   - **Convergent Validity**: Claude’s scoring aligned more closely with external standards, indicating strong convergent validity in analytic scoring.  
   - **Divergent Validity**: Both humans and GPT showed relatively low divergent validity, while Claude maintained more robust performance, though improvements are still needed.  

3. **Information Function and Discrimination**  
   - **Human Raters**: Covered a broader range of ability levels but lacked high discrimination within specific intervals.  
   - **Model Raters**: Excelled in specific ability ranges but showed decreased discrimination outside these zones, leading to variability.  

4. **Rater Effects**  
   - **Human Raters**: Tend to be more lenient and exhibit random scoring in analytic tasks involving multiple rubric dimensions.  
   - **Model Raters**: Display randomness in holistic scoring tasks, struggling to balance multiple textual features.  
   - **Conservative Scoring Patterns**: Both humans and models exhibit constrained scoring ranges, with models inheriting conservative tendencies from human-trained data.  
   - **Halo Effect**: Observed in both human and GPT raters, affecting divergent validity across rating dimensions.  

5. **Generalizability**  
   - The psychometric framework developed can be extended to other subjective scoring contexts, such as oral assessments and LLMs serving as judges, to further explore and refine their reliability and validity.

---

## Project Structure
```
├── repository/
│ ├── data/ # # Experimental data and sample files
│ │ ├── raw/ # Raw data with human raters' scores
│ │ ├── processed/ # Model scored data
│ │ │ ├── Essay_Set_#1/
│ │ │ ├── Essay_Set_#2/
│ │ │ └── Essay_Set_#3/
│ │ └── visualization # Data for visualization

│ ├── scripts/ # # Analysis scripts
│ │ ├── analysis/ # Analysis Files
│ │ │ ├── G_&_D_Study/ # G- and D-Study Analysis and Results Files
│ │ │ └── MFRM/ # Many Facet Rasch Model Analysis and Results Files
│ │ │ │ ├── Essay Set #1/
│ │ │ │ ├── Essay Set #2/
│ │ │ │ └── Essay Set #3/
│ │ │ │ │ ├── I&C
│ │ │ │ │ ├── Org
│ │ │ │ │ ├── V
│ │ │ │ │ ├── WC
│ │ │ │ │ ├── SF
│ │ │ │ │ └── Con1
│ │ ├── data_generation/ # Data Generation Codes
│ │ └── visualization/ # Visualization Codes

├── LICENSE # License information

├── README.md # Project documentation
```

---

## Installation and Usage

### Environment Requirements
- **Python**: 3.8+ (Anaconda recommended)
- **R**: 4.1.0+ (RStudio recommended)
- **Core Dependencies**:
  ```plaintext
  Python: numpy, pandas, scipy, scikit-learn, transformers, regex
  R: ggplot2, dplyr, patchwork, tidyr, ggsci, readxl, gridExtra
  ```
- **Hardware Requirements**:
  - 16GB+ RAM recommended (for large-scale text processing)

### Installation
1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/LLM-Writing-Assessment.git
   cd LLM-Writing-Assessment
   ```

2. **Install Python Dependencies**
   ```bash
   # Create conda environment (optional)
   conda create -n llm-assessment python=3.9
   conda activate llm-assessment

   # Install core packages
   pip install -r requirements.txt

   ```

3. **Install R Dependencies**
   ```R
   # Execute in R console
   install.packages(c("ggplot2", "dplyr", "patchwork", "tidyr", 
                    "ggsci", "readxl", "gridExtra", "extrafont"))

   # Install font support (requires admin rights)
   extrafont::font_import()
   ```

4. **Verify Installation**
   ```bash
   python scripts/verify_install.py
   Rscript scripts/verify_r_deps.R
   ```

### Usage
1. **Data Generation**
   - The raw data is stored in the `repository/data/raw` directory.
   - Run the Inference script to generate LLM scores.
   ```bash
   python repository/scripts/data_generation/Writing_Assessment.py
   ```

2. **G- and D- Study Analysis**
   - The data for the G-Study and D-Study is derived from the score samples obtained in the first step. Two human raters were selected to form the human rating group, while the first-round scores from GPT-4o-mini and GPT-4o were used to form the GPT rating group, and the first-round scores from Claude-3.5-Haiku and Claude-3.5-Sonnet were used to form the Claude rating group.
   - For Set #1 and Set #2, input the `.MANUAL` file name into `genova36.exe` and specify the output file name as `P_X_R_RESULT_...` to obtain the results. For Set #3, input the `.MANUAL` file name into `mGENOVA.exe`, and the output will be generated directly without the need to specify an output file name.
   - Click the `Source` button on the "D_Study_Results_Plot.R" code to visualize the D-Study Results.

3. **Regression Analysis**
   - The data for regression analysis is stored in the `repository/data/processed` directory.
   - Execute the regression script to evaluate the intra-rater reliability of each rater.
   ```bash
   python scripts/analysis/Regression.py
   ```

4. **Information**
   - The data for Information function visualization is stored in the `repository/data/visualization` directory.
   - Click the `Source` button on the `Information_Function_Plot.R` code to visualize the information function.
   - Execute the information function statics script to obtain the descriptive statistical components of the information function.
   ```bash
   python scripts/analysis/Info_Function_Statics.py
   ```

5. **Expected Item Characteristic Curves**
   - The data for Expected Item Characteristic Curve visualization is stored in the `repository/data/visualization` directory.
   - Click the `source` button on the `ICC_Function_Plot.R` code to visualize the Expected Item Characteristic Curves.

6. **Rating Scale Bar & Rater Probability Curves**
   - The data for Rating Scale Bar and Rater Probability Curve visualization is stored in the `repository/data/visualization`   
     directory.
   - Click the `source` button on the `Rating_Scale_Bar.R` code to visualize the Rating Scale Bar.
   - Execute the rater probability curve script to generate the visualization of the Rater Probability Curves.
   ```bash
   python scripts/analysis/Rater_Prob_Curve_Plot.py
   ```
7. **Overall Rating Frequency**
   - The data for Overall Rating Frequency visualization is stored in the `repository/data/visualization`   
     directory.
   - Click the `source` button on the `Rating_Scale_Bar.R` code to visualize the Rating Scale Bar.   
---

## Citations and References
When citing this project or using its resources in your research, please use the following format:

**BibTeX**
```bibtex
@misc{wang2025evaluating,
  title={Evaluating Large Language Models as Raters in Large-Scale Writing Assessments: A Psychometric Framework for Reliability and Validity},
  author={Yuehan Wang},
  year={2025},
  howpublished={\url{https://github.com/John-Wang-0809/LLM-Writing-Assessment-Psychometric-Framework}},
}
```

**APA**
```
Wang, Y. (2025). Evaluating Large Language Models as Raters in Large-Scale Writing Assessments: A Psychometric Framework for Reliability and Validity. Retrieved from https://github.com/John-Wang-0809/LLM-Writing-Assessment-Psychometric-Framework
```

---

## License
This project is licensed under the [MIT License](./LICENSE).

The MIT License permits free use, copying, and modification of the project, provided that the original license and copyright 
notice are retained. If you require different licensing terms, please modify the `LICENSE` file accordingly.

---

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m "Add Your Feature"
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a Pull Request**

Please ensure your code follows the project's coding standards and include relevant tests where applicable.

---

## Contact
For any questions or suggestions, please open an issue [here](https://github.com/John-Wang-0809/LLM-Writing-Assessment-Psychometric-Framework/issues) or contact [wangyuehan0809@163.com](wangyuehan0809@163.com).

Thank you for your interest and support in this project!
