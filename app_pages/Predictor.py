import os
import streamlit as st
import pandas as pd
import tensorflow as tf
import pickle


def predictor_body():
    important_features_file = os.path.join(os.getcwd(), "data", "important_features.pkl")
    model_folder = os.path.join(os.getcwd(), "data", "Model")
    clean_housing_data_file = os.path.join(os.getcwd(), "data", "clean_housing_data.pkl")

    with open(important_features_file,'rb') as f:
        features=pickle.load(f)

    formdata=pd.DataFrame()


    sample=pd.read_pickle(clean_housing_data_file).sample(1)




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
        model = tf.keras.models.load_model(model_folder, compile=False)
        model.compile(optimizer='adam',loss='mse',metrics=['mae'])
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