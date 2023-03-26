import os
import streamlit as st
import plotly.express as px
import pickle

def home_body():
    Y_test_prediction_file = os.path.join(os.getcwd(), "data", "Y_test_prediction.pkl")
    Y_train_prediction_file = os.path.join(os.getcwd(), "data", "Y_train_prediction.pkl")
    Y_test_file = os.path.join(os.getcwd(), "data", "Y_test.pkl")
    Y_train_file = os.path.join(os.getcwd(), "data", "Y_train.pkl")

    st.title('Data Analytics Project')

    st.header('Project overview')
    st.subheader('Project goals')
    st.markdown('The goal of this project is to create an analysis for an imaginary client in which the house prices and the correlation of the house features is analised, and to predict the prices of houses inherited by the client')
    st.subheader('The solution')
    st.markdown('My solution for the problem is to gather, analyse and clean the data. After that I have defined and implemetned a neural netwrok based machine learning model. I have trained the model on a subset of the cleaned data and tested it on the remained data')
    st.subheader('Results')


    with open(Y_test_prediction_file,'rb') as f:
        Y_test_prediction=pickle.load(f)
        f.close()

    with open(Y_train_prediction_file,'rb') as f:
        Y_train_prediction=pickle.load(f)
        f.close()
        
    with open(Y_test_file,'rb') as f:
        Y_test=pickle.load(f)
        f.close()
        
    with open(Y_train_file,'rb') as f:
        Y_train=pickle.load(f)
        f.close()

    fig=px.scatter({'Actual':list(Y_test),'Predicted':list(Y_test_prediction)},
            x='Actual',
            y='Predicted',
            range_x=[50_000,400_000],range_y=[50_000,400_000])

    fig.add_shape(type='line',
                    x0=70_000,
                    y0=70_000,
                    x1=380_000,
                    y1=380_000,
                    line=dict(color='Red',),
                    xref='x',
                    yref='y'
    )
    fig

    fig=px.scatter({'Actual':list(Y_train),'Predicted':list(Y_train_prediction)},
            x='Actual',
            y='Predicted',
            range_x=[50_000,400_000],range_y=[50_000,400_000])

    fig.add_shape(type='line',
                    x0=70_000,
                    y0=70_000,
                    x1=380_000,
                    y1=380_000,
                    line=dict(color='Red',),
                    xref='x',
                    yref='y'
    )
    fig

    r2_scores_file = os.path.join(os.getcwd(), "data", "r2_scores.pkl")
    with open(r2_scores_file,'rb') as f:
        r2_scores=pickle.load(f)
        f.close()

    st.markdown(f'R2 on test set: {r2_scores[0]}')
    st.markdown(f'R2 on train set: {r2_scores[1]}')
