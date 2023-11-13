import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk
st.set_page_config(
    page_title='price_predictior'
)
# loading the dataframe
with open('database/df.pkl','rb') as file:
    df=pk.load(file)
# loading the pipeline
with open('database/pipeline.pkl','rb') as file:
    pipeline=pk.load(file)
#st.dataframe(df)
# create form for  taking inputs
st.subheader('Enter your (Valid) property details')

# type
type=st.selectbox('Enter your property type',df['type'].unique().tolist())
#'''bedRoom bathroom
#     luxury balcony '''
sector=st.selectbox('Your prefeble sector',
    df['sector'].unique().tolist())
built_up_area=st.number_input('Your estimated area',help='Enter your area in sq-ft')
built_up_area=float(built_up_area)
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
pooja_room=st.selectbox('Do you want pooja room',options=[1,0])
pooja_room=int(pooja_room)
# 1-->yes,0-->no
servant_room=st.selectbox('Do you want servant room',options=[1,0])
servant_room=int(servant_room)
if st.button('Predict'):
    data=[[bedRoom, bathroom, balcony, floor_type, agePossession,
       sector, type, built_up_area, servant_room, pooja_room,
       furnishing_type, luxury]]
    column=['bedRoom', 'bathroom', 'balcony', 'floor_type', 'agePossession',
       'sector', 'type', 'built_up_area', 'servant room', 'pooja room',
       'furnishing_type', 'luxury']
    one_df=pd.DataFrame(data,columns=column)
    #conversion_dict = {'Yes': 1, 'No': 0}
   # one_df['bedRoom'] = one_df['bedRoom'].map(conversion_dict).astype(np.int64)
    #one_df['bathroom'] = one_df['bathroom'].map(conversion_dict).astype(np.int64)
    #st.dataframe(one_df)
    price=np.expm1(pipeline.predict(one_df))
    base_price=round(price[0],3)
    low_price=base_price
    # Display the prediction interval
    st.text(f'The estimated price for your property is around {base_price:.2f} cr.')
