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

# Loading the location dataframe
with open('database/location_df.pkl', 'rb') as file:
    df = pk.load(file)

# Convert the distance into meters
for i in df.columns:
    df[i] = df[i].apply(lambda x: x * 1000)

# Converting 0 into a large value
for i in df.columns:
    df[i] = df[i].apply(lambda x: 1000000 if x == 0 else x)

# Loading the cosine_similarity matrix
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
    rec = pd.DataFrame({
        'property_suggestion': top_property,
        'score': top_score
    })
    return rec

# Main content
st.subheader('Select any property to get recommendations')
property = st.selectbox(f'## Get recommendations on the basis of facilities, price and locality:',
                       df.index.unique().tolist(), index=None, placeholder='Select from the drop-down menu')

# Button to trigger search
search_button = st.button('Search')

# Initialize session state
if 'load_state' not in st.session_state:
    st.session_state.load_state = False

# Execute on search button click or load state
if search_button or st.session_state.load_state:
    st.session_state.load_state = True
    # Recommendation function
    similarity_matrix = 0.3 * facility_sim + 0.4 * price_sim + 0.3 * location_sim
    rec_df = recommendation(similarity_matrix, property)
    st.write("### Recommendations:")
    for i in rec_df['property_suggestion']:
        st.markdown(f'<span style="color:#1E90FF; font-size: 20px;">{i}</span>', unsafe_allow_html=True)
