import streamlit as st

# --- Page configuration ---
st.set_page_config(
    page_title="Gurgaon Home Value Predictor",
    page_icon="🏠",
    layout="wide"
)

# --- Custom sidebar styling ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #1e1e2f !important;
        color: white !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.title("Gurgaon Home Value Predictor")

# --- Summary Section ---
st.markdown("## Project Overview")
st.markdown("""
This application estimates residential property prices in Gurgaon using advanced machine learning techniques.  
It also recommends similar properties based on user preferences through a content-based recommendation system.

The goal of this project is to:
- Compare and evaluate different ML and DL models for property price prediction.
- Build a transparent and interpretable prediction pipeline.
- Provide a clean, interactive, and deployable solution using Streamlit.
""")

# --- About Role ---
st.markdown("## My Role in the Project")
st.markdown("""
As a final-year B.Tech student at IIIT Agartala with an interest in machine learning and deployment,  
I developed this project to apply the concepts I’ve learned and strengthen my practical understanding.

I was responsible for:
- Designing and training an XGBoost-based pipeline with custom feature engineering.
- Building a deep learning model (Custom ANN) and tuning it with Optuna.
- Using SHAP for interpreting machine learning model outputs.
- Creating an intuitive interface using Streamlit.
- Implementing a content-based recommender to suggest similar properties.
""")

# --- Model Comparison Section ---
st.markdown("## Model Performance Comparison")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**XGBoost + Feature Engineering (Best Performer)**")
    st.metric("R² Score", "0.89")
    st.metric("Mean Absolute Error", "7.5 Lakhs")
    st.metric("Root Mean Squared Error", "11.2 Lakhs")
    st.caption("Rich feature engineering and SHAP-based interpretation")

with col2:
    st.markdown("**Deep Learning (Custom ANN + Optuna)**")
    st.metric("R² Score", "0.80")
    st.metric("Mean Absolute Error", "8.6 Lakhs")
    st.metric("Root Mean Squared Error", "13.7 Lakhs")
    st.caption("Built using PyTorch with regularization techniques")

st.info(
    "While both models performed well, the XGBoost model offered ~9% higher accuracy and better interpretability. "
    "This made it more suitable for deployment and real-world use."
)

# --- Tech Stack Section ---
st.markdown("## Tools and Technologies Used")
st.markdown("""
- **Frontend**: Streamlit  
- **Machine Learning**: XGBoost, SHAP  
- **Deep Learning**: PyTorch, Optuna  
- **Preprocessing**: Scikit-learn ColumnTransformer, Category Encoders  
- **Data Visualization**: Matplotlib, Seaborn  
- **Deployment**: Streamlit Cloud
""")

# --- App Navigation Info ---
st.markdown("## App Modules")
st.markdown("""
1. **Machine Learning Predictor** – Uses XGBoost with SHAP explanations  
2. **Deep Learning Predictor** – Custom ANN model built and tuned using PyTorch + Optuna  
3. **Property Recommendation System** – Content-based filtering to suggest similar properties
""")

# --- Contact Section ---
st.markdown("## Connect with Me")
st.markdown("""
If you're interested in discussing this project, giving feedback, or exploring collaboration, feel free to connect:

- **GitHub**: [github.com/Abhijeetkashyap-ds87](https://github.com/Abhijeetkashyap-ds87)  
- **LinkedIn**: [linkedin.com/in/abhijeetkashyap-ds](https://www.linkedin.com/in/abhijeet-kashyap-250293233/)
""")
