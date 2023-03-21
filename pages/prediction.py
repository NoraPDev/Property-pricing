import streamlit as st
import pandas as pd
import keras
import pickle

st.title('Sales Price Prediction')

with open('data\important_features.pkl','rb') as f:
    features=pickle.load(f)

inhereted = pd.read_pickle('data\inhereted_houses_corr.pkl')[features]
st.header('Inhereted houses')
st.write(inhereted)

model = keras.models.load_model('data\Model')
prediction=model.predict(inhereted)
inhereted_with_prediction=pd.DataFrame(inhereted)
inhereted_with_prediction['predicted SalePrice']=prediction
st.header('Inhereted houses prediction')
st.write(inhereted_with_prediction)