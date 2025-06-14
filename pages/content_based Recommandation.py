import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk

# Set page configuration
st.set_page_config(
    page_title='Property Recommendation',
    page_icon="✨",
    layout="wide",
)

# Custom CSS for sidebar styling
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #1e1e2f !important;
        color: white !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    .stButton > button {
        background-color: #00b300;
        color: white;
        border-radius: 5px;
        font-weight: bold;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Load data
with open('database/location_df.pkl', 'rb') as file:
    df = pk.load(file)

# Convert distances
for col in df.columns:
    df[col] = df[col].apply(lambda x: x * 1000 if x != 0 else 1_000_000)

# Load similarity matrices
with open('database/facility.pkl', 'rb') as matrix1:
    facility_sim = pk.load(matrix1)
with open('database/location.pkl', 'rb') as matrix2:
    location_sim = pk.load(matrix2)
with open('database/price.pkl', 'rb') as matrix3:
    price_sim = pk.load(matrix3)

# Recommendation function
def recommendation(sim_matrix, property_name):
    sim_score = list(enumerate(sim_matrix[df.index.get_loc(property_name)]))
    sorted_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_score[1:6]]
    top_score = [i[1] for i in sorted_score[1:6]]
    top_property = df.index[top_indices].tolist()
    return pd.DataFrame({
        'property_suggestion': top_property,
        'score': top_score
    })

# UI
st.subheader('🏠 Select any property to get recommendations')
property = st.selectbox(
    '## Based on facilities, price, and locality:',
    df.index.unique().tolist(),
    index=None,
    placeholder='Select from the drop-down menu'
)
search_button = st.button('🔍 Search')

# Session state initialization
if 'load_state' not in st.session_state:
    st.session_state.load_state = False

if search_button:
    if property is None:
        st.warning("⚠️ Please select a property from the dropdown before searching.")
        st.session_state.load_state = False
    else:
        st.session_state.load_state = True

# Only display recommendations if load_state is True and a property is selected
if st.session_state.load_state and property is not None:
    sim_matrix = 0.3 * facility_sim + 0.4 * price_sim + 0.3 * location_sim
    rec_df = recommendation(sim_matrix, property)
    st.write("### 🏡 Top 5 Recommended Properties:")
    for i in rec_df['property_suggestion']:
        st.markdown(f'<span style="color:#1E90FF; font-size: 20px;">{i}</span>', unsafe_allow_html=True)
