import streamlit as st

def custom_box_template(text, style):
    """
    Create a custom box template for different styles of text.
    """
    st.markdown(
        f"""
        <style>
        .{style} {{
            padding: 20px;
            border-radius: 10px;
        }}
        </style>
        """
        , unsafe_allow_html=True
    )

    st.markdown(f'<div class="{style}">{text}</div>', unsafe_allow_html=True)

# Store project description in a variable
project_description = """👋   Hi!    


Welcome to the Gurgaon Home Value Predictor project! I have been working diligently on my first part of capstone project to develop a robust model using the ExtraTrees Regressor to predict flat prices in Gurgaon. This project is a culmination of my skills and knowledge in data science and real estate analytics, and may be it is a stepping stone towards my professional growth.
By incorporating advanced techniques like feature engineering and utilizing the Random Forest Regressor for feature selection, I have created a powerful model that accurately captures the nuances of the real estate market. The model takes into account essential features such as location, square footage, and number of bedrooms to generate precise estimates of flat prices in Gurgaon.
Enter valid inputs to see the performance of model
I am actively seeking collaboration opportunities to further enhance my skills and expand my knowledge in the realms of data science 

If you have any potential projects or opportunities, please feel free to contact me at [abhijeetkashyapak8789@gmail.com]. I am eager to collaborate and contribute to the world of data-driven real estate analysis.

Thank you for your support, and I look forward to connecting with like-minded individuals who share my passion for data science . Let's make a difference together!
"""

# Display the black box template with the project description
custom_box_template(project_description, 'black-box')

# Display the green box for the specific text
custom_box_template("Recommender system for flats in Gurgaon is coming soon!", 'green-box')

