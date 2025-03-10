import streamlit as st
import pandas as pd
import numpy as np

st.title('Group A: Team 2') 
st.subheader('Members:')
col1, col2 = st.columns(2, vertical_alignment = 'center')
with col1:
    st.markdown('🧒🏻 Sangay Lakshay Yangzom')
    st.markdown('🧔🏻‍♂️ Chandra Man Limbu')
    
with col2:
    st.markdown('👱🏻‍♀️ Nob Gyem')
    st.markdown('👱🏻 Kinzang Dorji')
st.markdown('👩🏻‍🦳 Kinley Pem')

st.subheader('Project Description:')
st.markdown('The project is about predicting the number of overnight visitors in Bhutan. The dataset is collected from the UN Data and had been preprocessed and cleaned. The dataset contains the following columns:')
st.markdown('Dataset:')    
data = pd.read_csv('cleanedData.csv')    
st.write(data.head())
st.markdown('Link to GitHub Repository:')
st.page_link("https://github.com/Sangay-Lakshay/BhutanTourismProject", label="GitHub", icon="➡️")
st.markdown('The model used for prediction is a Random Forest Regressor model. The model is trained on the dataset and the model is saved as a pickle file. The model is then loaded and used to predict the number of overnight visitors based on the user input. The user can input the following features to predict the number of overnight visitors:')
st.markdown('1. Year')
st.markdown('2. Air Travel')
st.markdown('3. Land Travel')
st.markdown('4. Travel Expenditure')
st.markdown('5. Passenger Transport Expenditure')
st.markdown('6. Number of Establishments')
st.markdown('7. Number of Rooms')
st.markdown('8. Number of Bed Places')
st.markdown('The user can input the above features and click on the predict button to get the prediction for the number of overnight visitors.')