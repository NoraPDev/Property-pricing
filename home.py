import sklearn
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle

st.title('Data Analytics Project')

st.header('Project overview')
st.subheader('Project goals')
st.markdown('The goal of this project is to create an analysis for an imaginary client in which the house prices and the correlation of the house features is analised, and to predict the prices of houses inhereted by the client')
st.subheader('The solution')
st.markdown('My solution for the problem is to gather, analyse and clean the data. After that I have defined and implemetned a neural netwrok based machine learning model. I have trained the model on a subset of the cleaned data and tested it on the remained data')
st.subheader('Results')

