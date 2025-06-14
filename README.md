# Gurgaon Home Value Predictor App

## Overview

The Gurgaon Home Value Predictor App is a machine learning-based application designed to estimate residential property prices in Gurgaon. It also provides recommendations for similar properties based on selected features. The goal of this project is to explore model performance differences between traditional ML models and deep learning approaches, while also focusing on deployment and user experience.

---

## Features

- Property value prediction using user-input details such as location, size, and amenities  
- Comparison of model outputs from XGBoost and a deep learning ANN  
- SHAP-based interpretability for the machine learning predictions  
- Content-based recommender system for suggesting similar properties  
- Streamlit-based frontend for an interactive user experience

---

## Model Comparison

| Metric                  | XGBoost + Feature Engineering | Custom ANN (PyTorch + Optuna) |
|-------------------------|------------------------------|-------------------------------|
| R² Score                | 0.89                          | 0.80                          |
| Mean Absolute Error     | 7.5 Lakhs                     | 8.6 Lakhs                     |
| Root Mean Squared Error | 11.2 Lakhs                    | 13.7 Lakhs                    |

The XGBoost model, enhanced with engineered features and SHAP interpretability, outperformed the deep learning model by approximately 9% in R² score. It also exhibited better error metrics, making it the more reliable model in this context.

---

## Technical Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Machine Learning:** XGBoost, SHAP  
- **Deep Learning:** PyTorch with Optuna  
- **Preprocessing:** ColumnTransformer, Category Encoders  
- **Visualization:** Seaborn, Matplotlib  
- **Deployment:** Streamlit (local and deployable to cloud)

---

## Methodology

- Data cleaning and preprocessing using Pandas and regular expressions  
- Feature engineering using domain knowledge and clustering approaches  
- Feature importance analysis via SHAP and permutation methods  
- Hyperparameter tuning with RandomizedSearchCV for ML and Optuna for DL  
- Separate pipelines for ML and DL to enable model comparison  
- Recommendation logic based on a hybrid similarity score combining price, facilities, and location

---

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/GurgaonHomeValuePredictorApp.git

# Navigate to the project directory
cd GurgaonHomeValuePredictorApp

# Install required packages
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
