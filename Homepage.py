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
st.title("🏠 Gurgaon Home Value Predictor")

# --- Summary Section ---
st.markdown("""
### 🎯 Project Overview
This app predicts **residential property prices in Gurgaon** using state-of-the-art machine learning techniques.  
It also recommends similar properties using a content-based recommender system.

The project was designed to:
- Compare different ML and DL approaches
- Identify the most **accurate and interpretable model**
- Provide a seamless and interactive deployment experience
""")

# --- Your Role ---
st.markdown("### 👨‍💻 My Contributions")
st.markdown("""
- Built an end-to-end pipeline using **XGBoost with engineered features**  
- Developed a **Custom ANN** and tuned it with **Optuna**  
- Implemented **SHAP** to interpret the ML model's predictions  
- Deployed the app with a clean UI using **Streamlit Cloud**  
- Integrated a **content-based property recommender**
""")

# --- Model Comparison Section ---
st.markdown("### 📊 Model Performance Comparison")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### ✅ Best Model: XGBoost + Feature Engineering")
    st.metric("R² Score", "0.89")
    st.metric("MAE", "7.5 Lakhs")
    st.metric("RMSE", "11.2 Lakhs")
    st.caption("• Advanced feature engineering\n• SHAP-based interpretability")

with col2:
    st.markdown("#### 🧠 Deep Learning (Custom ANN + Optuna)")
    st.metric("R² Score", "0.80")
    st.metric("MAE", "8.6 Lakhs")
    st.metric("RMSE", "13.7 Lakhs")
    st.caption("• Custom ANN tuned with Optuna\n• Dropout and batch normalization")

st.info("📌 **XGBoost model outperformed Deep Learning by ~9%** in accuracy (R²). It also provided better interpretability using SHAP.")

# --- Tech Stack Section ---
st.markdown("### 🛠️ Tech Stack Used")
st.markdown("""
- **Frontend**: Streamlit  
- **ML Model**: XGBoostRegressor + SHAP  
- **DL Model**: Custom ANN built with PyTorch and tuned via Optuna  
- **Preprocessing**: ColumnTransformer, Category Encoders  
- **Visualization**: Matplotlib, Seaborn  
- **Deployment**: Streamlit Cloud
""")

# --- Navigation Info ---
st.markdown("### 📁 Explore the App")
st.markdown("""
1. 🤖 **Machine Learning Predictor** – XGBoost + SHAP explanations  
2. 🧠 **Deep Learning Predictor** – Custom ANN (PyTorch + Optuna)  
3. 🏡 **Property Recommender** – Content-based filtering  
""")

# --- Contact / GitHub ---
st.markdown("### 🔗 Connect With Me")
st.markdown("""
- GitHub: [github.com/your-profile](https://github.com/Abhijeetkashyap-ds87)  
""")
