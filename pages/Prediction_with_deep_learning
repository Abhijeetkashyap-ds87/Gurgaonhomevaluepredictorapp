import torch
import torch.nn as nn
import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk
import joblib

st.set_page_config(
    page_title="Deep Learning Predictor",
    page_icon="🤖",
    layout="wide"
)
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


class MyAnn(nn.Module):
  def __init__(self,input_dim):
    super().__init__()

    # Intializing layers in sequential container
    self.model=nn.Sequential(
        # ist layer
        nn.Linear(out_features=12,in_features=input_dim),
        nn.BatchNorm1d(12,affine=True),
        nn.ReLU(),

        # 2nd layer
        nn.Linear(out_features=10,in_features=12),
        nn.BatchNorm1d(10,affine=True),
        nn.ReLU(),

        # 3rd layer
        nn.Linear(out_features=8,in_features=10),
        #nn.Dropout1d(p=0.2),
        nn.BatchNorm1d(8,affine=True),
        nn.ReLU(),

        # 4th layer
        nn.Linear(out_features=6,in_features=8),
        nn.BatchNorm1d(6,affine=True),
        nn.ReLU(),

        # 5th layer
        nn.Linear(out_features=4,in_features=6),
        nn.BatchNorm1d(4,affine=True),
        nn.ReLU(),
        # output
        nn.Linear(out_features=1, in_features=4)
      )

  def forward(self,train_data):
    output= self.model(train_data)
    return output.squeeze(1)



# on saving model torch only save the weiights i.e model.state_dict()
# Set page configuration

with open('database/modified_df.pkl','rb') as file:
    df=pd.read_pickle(file)
    
# loading transformer
transformation = joblib.load('database/transformer_version.pkl')


# Loading model
model_=MyAnn(15) # making instance
state_dict = torch.load('database/ann_model.pt', map_location=torch.device('cpu')) #  loading weights and baises of model
model_.load_state_dict(state_dict) # getting weights and baises of model

# create form for  taking inputs
st.title("Deep Learning Based Price Prediction")
st.markdown("Upload your property features and get an instant estimate.")
with st.form('Enter your (Valid) property details'):
    #st.subheader('Property Price Predictor')
    st.subheader('Enter your (Valid) property details')
    # type
    type=st.selectbox('Enter your property type',df['type'].unique().tolist())
    #bedRoom bathroom
    #     luxury balcony 
    sector=st.selectbox('Your prefeble sector',
        df['sector'].unique().tolist())
    built_up_area=st.number_input('Your estimated area',placeholder='Enter your area in sq-ft',min_value=30.00,max_value=15000.00,step=1.,format="%2.1f")
   # built_up_area=float(built_up_area)
    agePossession=st.selectbox('How old property are you looking',
        df['agePossession'].unique().tolist()
    )
    #2-->unfurnished,1-->furnished,0-->semifurnished
    furnishing_type=st.selectbox('Which type of furnishing you want',
        df['furnishing_type'].unique().tolist()
    )
    luxury=st.selectbox('Which type of luxury you want',df['luxury'].unique().tolist())
    # floor_type
    floor_type=st.selectbox('Your prefeble floor',
        df['floor_type'].unique().tolist()
    )
    balcony=st.selectbox('How many balcony you prefer',df['balcony'].unique().tolist())
    bedRoom=float(st.selectbox('BHK',sorted(df['bedRoom'].unique().tolist())))
    bathroom=float(st.selectbox('Bathroom',sorted(df['bathroom'].unique().tolist())))
    pooja_room=st.selectbox('Do you want pooja room',df['pooja room'].unique().tolist())

    # 1-->yes,0-->no
    servant_room=st.selectbox('Do you want servant room',df['servant room'].unique().tolist())

    if st.form_submit_button('Predict'):
        data=[[bedRoom, bathroom, balcony, floor_type, agePossession,
        sector, type, built_up_area, servant_room, pooja_room,
        furnishing_type, luxury]]
        column=['bedRoom', 'bathroom', 'balcony', 'floor_type', 'agePossession',
       'sector', 'type', 'built_up_area', 'servant room', 'pooja room',
       'furnishing_type', 'luxury']
        one_df=pd.DataFrame(data,columns=column)

        # apply transformation then model
        one_df=transformation.transform(one_df)
        #st.dataframe(one_df)
        # predicting
        model_.eval() # Inferencing mode
        with torch.inference_mode():
            input_tensor=torch.tensor(one_df,dtype=torch.float32)
            price=torch.expm1(model_(input_tensor)).detach().numpy() 
            base_price=round(price[0],3)
            low_price=base_price
            # Display the prediction interval
            st.markdown(
                f'<div style="font-size: 18px; font-weight: bold; color: White;">The estimated price for your property is around {base_price:.2f} cr.</div>',
                unsafe_allow_html=True)
    css="""
    <style>
        [data-testid="stForm"] {
            background: Grey;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
