import os
import streamlit as st
import pandas as pd
from tensorflow import keras
import pickle

def prediction_body():
    important_features_file = os.path.join(os.getcwd(), "data", "important_features.pkl")
    inherited_houses_corr_file = os.path.join(os.getcwd(), "data", "inherited_houses_corr.pkl")
    model_folder = os.path.join(os.getcwd(), "data", "Model")
    st.title('Sales Price Prediction')

    with open(important_features_file,'rb') as f:
        features=pickle.load(f)

    inherited = pd.read_pickle(inherited_houses_corr_file)[features]
    st.header('Inherited houses')
    st.write(inherited)
    
    model = keras.models.load_model(model_folder)
   
    prediction=model.predict(inherited)
    inherited_with_prediction=pd.DataFrame(inherited)
    inherited_with_prediction['predicted SalePrice']=prediction
    st.header('Inherited houses prediction')
    st.write(inherited_with_prediction)