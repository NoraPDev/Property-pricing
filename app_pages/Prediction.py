import streamlit as st
import pandas as pd
from tensorflow import keras
import pickle

def prediction_body():
    st.title('Sales Price Prediction')

    with open('data\important_features.pkl','rb') as f:
        features=pickle.load(f)

    inherited = pd.read_pickle('data\inherited_houses_corr.pkl')[features]
    st.header('Inherited houses')
    st.write(inherited)

    model = keras.models.load_model('data\Model')
    prediction=model.predict(inherited)
    inherited_with_prediction=pd.DataFrame(inherited)
    inherited_with_prediction['predicted SalePrice']=prediction
    st.header('Inherited houses prediction')
    st.write(inherited_with_prediction)