# GurgaonHomeValuePredictorApp

## Overview
The GurgaonHomeValuePredictorApp is designed to predict property values in Gurgaon based on various features such as location, size, and amenities. The app leverages machine learning algorithms to provide accurate and reliable predictions, helping users make informed real estate decisions.

## Features
- **User Input Interface**: Allows users to input property details like location, size, and amenities.
- **Predictive Model**: Utilizes advanced machine learning models to predict the property value based on input features.
- **Interactive Visualizations**: Displays prediction results along with key insights and trends in the Gurgaon real estate market.
- **Streamlit Deployment**: The app is deployed using Streamlit, providing an easy-to-use web interface accessible on any device.

## Tech Stack
- **Frontend**: Streamlit for a seamless and interactive web-based user experience.
- **Backend**: Python handling data processing and model predictions.
- **Machine Learning**: XGBoost for regression analysis and model predictions.
- **Data Visualization**: Matplotlib and Seaborn for generating visual insights.
## Methods Used
- **Data Cleaning****: Utilized regular expressions and pandas for effective data cleaning.
- **Feature Engineering**: Created new columns based on clustering algorithms to enhance model performance.
- **Feature Extraction**: Employed tree-based feature extraction methods and used SHAP, permutation, and combination techniques for extracting impactful features.
- **Model Selection**: Explored Extra Tree Regressor and XGBoost Regressor. Chose XGBoost Regressor and performed randomized search CV and cross-validation for a good bias-variance trade-off.


## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GurgaonHomeValuePredictorApp.git
2. Navigate to the project directory:
   ```bash
   cd GurgaonHomeValuePredictorApp
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Streamlit app::
   ```bash
   streamlit run app.py


