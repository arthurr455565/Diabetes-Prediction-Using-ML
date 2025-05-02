# Diabetes Prediction Model 🩺

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabetes-prediction-using-ml.streamlit.app)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An interactive web application that uses machine learning to predict diabetes risk based on health metrics. Built with Streamlit and featuring an elegant, modern UI with real-time visualizations.

## Live Demo

**Try it now:** [Diabetes Prediction App](https://diabetes-prediction-using-ml.streamlit.app)

![App Screenshot](image/app_screenshot.jpg)

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [UI & UX Design](#ui--ux-design)
4. [Dataset](#dataset)
5. [Model](#model)
6. [Installation](#installation)
7. [How It Works](#how-it-works)
8. [Project Structure](#project-structure)
9. [Explanation Methods](#explanation-methods)
10. [Model Performance](#model-performance)
11. [Project Motivation](#project-motivation)
12. [Contributing](#contributing)
13. [License](#license)
14. [Contact](#contact)

---

## Overview

The **Diabetes Prediction with AI** project leverages machine learning to predict diabetes risk from simple health metrics. The application provides:

- **Real-time predictions** based on user-provided health data
- **Interactive visualizations** that explain model decisions
- **Modern, responsive UI** designed for excellent user experience
- **Clinical insights** presented in an accessible manner

> **Note:** This model is for educational and experimental purposes only. It has not been reviewed by medical professionals and should not replace medical advice.

### Why This Project?

Early risk assessment can significantly improve diabetes outcomes. This project demonstrates:
- Practical application of machine learning in healthcare
- Advanced model interpretability through SHAP and permutation importance
- Modern web application design and deployment
- Responsible AI with clear explanations of predictions

---

## Features

### ✨ Core Features
- **Interactive Health Data Input** - User-friendly forms with validation
- **Instant Prediction Results** - Real-time risk assessment with probability
- **Advanced Visualizations** - Charts and graphics to explain predictions
- **Model Explainability** - SHAP and permutation importance visualizations
- **Professional UI/UX** - Modern, responsive design with animations and intuitive layout

### 🎨 UI & UX Features
- **Animated Loading Screen** - Provides visual feedback during processing
- **Interactive Form Elements** - Tooltips, validation, and instant feedback
- **Color-Coded Results** - Clear visual indicators of risk assessment
- **Responsive Layout** - Adapts to different screen sizes
- **Intuitive Information Architecture** - Well-organized content sections
- **Visual Hierarchy** - Important information stands out through design
- **Accessibility Considerations** - Readable text, clear contrast, and descriptive elements

---

## UI & UX Design

The application features a professionally designed user interface with:

### Design Elements
- **Color Scheme** - Blue and white primary palette with contextual colors for risk indicators
- **Typography** - Clean, readable Inter font family with appropriate hierarchy
- **Card-Based Layout** - Information organized in distinct sections for clarity
- **Data Visualization** - Donut charts, risk meters, and SHAP plots for intuitive understanding
- **Micro-interactions** - Subtle animations and hover effects for enhanced engagement

### User Experience
- **Guided Flow** - Clear progression from input to results to explanation
- **Instant Feedback** - Real-time responses to user interactions
- **Educational Content** - Informative sections about diabetes and risk factors
- **Contextual Help** - Tooltips and explanations for technical terms
- **Responsive Design** - Optimized for various devices and screen sizes

---

## Dataset

The dataset is from the **National Institute of Diabetes and Digestive and Kidney Diseases** and includes:

### General Overview
- **Number of rows:** 768
- **Number of columns:** 9
- **Column names and data types:**
  - `Pregnancies` (int64): Number of times pregnant.
  - `Glucose` (int64): Plasma glucose concentration after 2 hours in an oral glucose tolerance test.
  - `BloodPressure` (int64): Diastolic blood pressure (mm Hg).
  - `SkinThickness` (int64): Triceps skin fold thickness (mm).
  - `Insulin` (int64): 2-Hour serum insulin (mu U/ml).
  - `BMI` (float64): Body mass index (weight in kg/(height in m)^2).
  - `DiabetesPedigreeFunction` (float64): Diabetes pedigree function.
  - `Age` (int64): Age (years).
  - `Outcome` (int64): Class variable (0 or 1).

#### For prediction, we use only:
- `Pregnancies`
- `Glucose` 
- `BMI`
- `Insulin`
- `Age`

---

## Model

The prediction model uses a `RandomForestClassifier` selected through rigorous experimentation. Key aspects include:

- **Model Selection**: Chosen based on ROC AUC performance
- **Hyperparameter Optimization**: Tuned using Optuna
- **Feature Engineering**: Custom transformers for optimal feature representation
- **Cross-Validation**: Ensures reliable performance on unseen data
- **Threshold Adjustment**: Optimized for Recall due to the medical context

### Transformation Pipeline
1. **FeatureEngineering**: Creates derived features and handles missing data
2. **WoEEncoding**: Applies Weight of Evidence encoding to improve predictive power
3. **ColumnSelector**: Selects the most relevant features for prediction

> Detailed model information is available in [the model notebook](notebooks/Model.ipynb).

---

## Installation

### Prerequisites
- Python 3.10 or above
- Pip package manager

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/arthurr455565/Diabetes-Prediction-Using-ML.git
   cd Diabetes-Prediction-Using-ML
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run main.py
   ```

5. **Access in browser:**
   The application will be available at [http://localhost:8501](http://localhost:8501)

---

## How It Works

### Application Workflow
1. **User Input**:
   - Enter health data in the sidebar form
   - Parameters include Pregnancies, Glucose, Insulin, BMI, and Age
   
2. **Data Processing**:
   - Input is validated and processed
   - Features are transformed according to the model pipeline
   
3. **Prediction Generation**:
   - The model predicts diabetes risk probability
   - Results are visualized with appropriate risk indicators
   
4. **Result Explanation**:
   - SHAP visualizations explain feature contributions
   - Permutation importance shows global feature impact
   
5. **Additional Information**:
   - Model performance metrics display reliability
   - Educational content provides context about diabetes

---

## Project Structure
```
Diabetes-Prediction-Using-ML/
├── README.md                 # Project documentation
├── main.py                   # Entry point for the Streamlit app
├── loader.py                 # Data loading and preprocessing
├── training.py               # Script for training the model
├── requirements.txt          # Project dependencies
├── LICENSE                   # License file
├── .streamlit/               # Streamlit configuration
│   └── config.toml           # Streamlit theme and settings
├── datasets/                 # Dataset directory
│   └── diabetes.csv          # Dataset used for training and predictions
├── model.pkl                 # Trained machine learning model
├── image/                    # Application images
│   └── page_icon.jpeg        # Application page icon
├── data/                     # Data configuration and static content
│   ├── config.py             # Configuration variables
│   └── base.py               # Static HTML/CSS content
├── function/                 # Utility functions
│   └── function.py           # Helper functions for visualization and data processing
└── app/                      # Application components
    ├── about.py              # Informational content about diabetes
    ├── explainer.py          # SHAP explanation visualizations
    ├── header.py             # Application header component
    ├── input.py              # User input form component
    ├── performance.py        # Model performance metrics visualization
    ├── perm_importance.py    # Permutation importance visualization
    └── predict.py            # Prediction logic and results display
```

---

## Explanation Methods

The application provides multiple ways to understand predictions:

### 1. SHAP (SHapley Additive exPlanations)
- **Waterfall Plot**: Shows how each feature contributes to pushing the prediction higher or lower
- **Force Plot**: Interactive visualization showing the impact of each feature value

### 2. Permutation Importance
- Measures how model performance decreases when a feature is randomly shuffled
- Helps identify which features are most critical for accurate predictions

### 3. Risk Visualization
- **Risk Meter**: Linear gauge showing the predicted probability
- **Donut Chart**: Circular visualization of risk percentage
- **Contextual Recommendations**: Personalized guidance based on prediction results

---

## Model Performance

Performance metrics displayed in the application:

| Metric | Value | Description |
|--------|-------|-------------|
| **Accuracy** | 0.7857 | Percentage of correct predictions |
| **Precision** | 0.6296 | Ratio of true positives to total positive predictions |
| **Recall** | 0.9444 | Ratio of true positives to total actual positives |
| **F1 Score** | 0.7556 | Harmonic mean of Precision and Recall |
| **ROC AUC** | 0.8367 | Area under the ROC curve |

> The model prioritizes Recall (minimizing false negatives) due to the medical context where missing a potential diabetes case would be more problematic than a false positive.

---

## Project Motivation

This project was developed to:
- Apply machine learning to solve a meaningful healthcare problem
- Demonstrate best practices in model interpretability
- Create an engaging, user-friendly interface for AI applications
- Showcase responsible AI development with clear explanations
- Provide educational value about diabetes risk factors

---

## Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and add meaningful commit messages
4. **Push to your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a pull request** with a detailed description of your changes

Please ensure your code follows the project's style guidelines and includes appropriate tests.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

### Bishal Roy
- 📧 **Email**: bishalroy909@gmail.com
- 💼 **LinkedIn**: [Bishal Roy](https://www.linkedin.com/in/bishal-roy-028386193/)
- 🐙 **GitHub**: [arthurr455565](https://github.com/arthurr455565)

Feel free to reach out with questions, suggestions, or collaboration opportunities!

