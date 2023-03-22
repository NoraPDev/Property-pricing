import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from tensorflow import keras
import tensorflow as tf
import pickle

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