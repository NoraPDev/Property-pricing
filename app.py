'''
This file and the contents have been taken from the
 Churnometer Walkthrough Project 2 and customised for
 this project
'''
import streamlit as st

from app_pages.multi_page import MultiPage

# load pages scripts
from app_pages.Home import home_body
from app_pages.Analysis import analysis_body
from app_pages.Prediction import prediction_body
from app_pages.Predictor import predictor_body

# Create an instance of the app
app = MultiPage(app_name="Price Predictor - Houses")

# Add your app pages here using .add_page()
app.add_page("Home", home_body)
app.add_page("Analysis", analysis_body)
app.add_page("House Sale Price Prediction", prediction_body)
app.add_page("Price Predictor", predictor_body)

app.run()  # Run the app
