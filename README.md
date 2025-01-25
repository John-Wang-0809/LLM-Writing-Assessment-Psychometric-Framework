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
1. **Data Preparation**
   - Place writing samples and human scoring results in the `data/` directory.
   - Ensure data formats align with the scripts' requirements.

2. **Model Inference**
   - Run the inference script to generate LLM scores.
   ```bash
   python scripts/run_inference.py
   ```

3. **Psychometric Analysis**
   - Execute the analysis script to evaluate reliability and validity using G-Theory and MFRM.
   ```bash
   python scripts/psychometric_analysis.py
   ```

4. **Visualization**
   - Generate visualizations for score consistency and information functions.
   ```bash
   python scripts/visualize_results.py
   ```

---

## Citations and References
When citing this project or using its resources in your research, please use the following format:

**BibTeX**
```bibtex
@misc{yourname2025evaluating,
  title={Evaluating Large Language Models as Raters in Large-Scale Writing Assessments: A Psychometric Framework for Reliability and Validity},
  author={Your Name},
  year={2025},
  howpublished={\url{https://github.com/your-username/LLM-Writing-Assessment}},
}
```

**APA**
```
Your Name. (2025). Evaluating Large Language Models as Raters in Large-Scale Writing Assessments: A Psychometric Framework for Reliability and Validity. Retrieved from https://github.com/your-username/LLM-Writing-Assessment
```

**References**
1. Bachman, L. F. (1990). *Fundamental considerations in language testing*. Oxford University Press.
2. Brennan, R. L. (2001). *Generalizability theory*. Springer.
3. McNamara, T. (1996). *Measuring second language performance*. Longman.
4. ... *(Add additional references as needed)*

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
For any questions or suggestions, please open an issue [here](https://github.com/your-username/LLM-Writing-Assessment/issues) or contact [your.email@example.com](mailto:your.email@example.com).

Thank you for your interest and support in this project!
