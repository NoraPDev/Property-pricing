import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from tensorflow import keras
import tensorflow as tf
import pickle

first=False

with open('data\important_features.pkl','rb') as f:
    features=pickle.load(f)

formdata=pd.DataFrame()


sample=pd.read_pickle('data\clean_housing_data.pkl').sample(1)




with st.form('form'):
    st.write("House details")
    importatnt_inputs={}
    for f in features:
        if f not in st.session_state:
            importatnt_inputs[f]=st.number_input(f,value=sample[f].iloc[0])
            st.session_state[f]=sample[f].iloc[0]
        else:
            importatnt_inputs[f]=st.number_input(f,value=st.session_state[f])
    
    inputs=importatnt_inputs
    model = keras.models.load_model('data\Model')
    submitted = st.form_submit_button("Submit")
    if submitted:
        formdata=pd.DataFrame(importatnt_inputs,index=[1])
        prediction= model.predict(formdata)
        formdata['Predicted SalePrice']=prediction
        if 'fdata' in st.session_state:
            formdata=pd.concat([formdata,st.session_state['fdata']])
        st.session_state['fdata']=formdata
        st.write(prediction)
        


formdata