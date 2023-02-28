import matplotlib.pyplot as plt
import streamlit as st
from datetime import date
import pandas as pd
from PIL import Image
import pickle

st.title('cement sales Forecasting')  

st.sidebar.title("About")
st.sidebar.info("Forecastingcement sales 'Prophet' Machine Learning model.")

def get_input():
	st.sidebar.header("Input From user")
	st.sidebar.subheader("Select range of Date for visualize data for particular date range.")
	st.sidebar.write("(From 2023-01-31 to 2023-12-31)")
	start_date = st.sidebar.text_input("Start Date", "2023-01-31")
	end_date = st.sidebar.text_input("End Date", "2023-12-31")
	st.write("")
	st.sidebar.subheader("Enter Period for Forecasting of Price")
	period = st.sidebar.text_input("Period (In months)", "12")
	return start_date, end_date, period
    
    
    
    
    
