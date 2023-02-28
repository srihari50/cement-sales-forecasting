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

START = "2023-01-31"
TODAY = date.today().strftime("%Y-%M-%d")

def get_data(start, end):
	df = pd.read_excel('C:\Users\sriha\Desktop\cement project\All India_Features.xlsx')
	start = pd.to_datetime(start)
	end = pd.to_datetime(end)
	start_row = 0
	end_row = 0

	for i in range(0, len(df)):
		if start <=	pd.to_datetime(df['Date'][i]):
			start_row = i
			break
	for j in range(0, len(df)):
		if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
			end_row = len(df) - 1 - j
			break

	df = df.set_index(pd.DatetimeIndex(df['Date'].values))
	return df.iloc[start_row:end_row+1, :]

start, end, period = get_input()
data = get_data(start, end)

st.subheader("Data")
st.write("First 5 Columns")
st.write(data.head())
st.write("Last 5 Columns")
st.write(data.tail())
   
st.subheader('Close Price')
st.write("Zoom In/Zoom Out for better visualization.")
st.line_chart(data[['Sales_Quantity_Billiontonnes', 'Order_Quantity_Billiontonnes']])

st.subheader("Volume")
st.write("Zoom In/Zoom Out for better visualization.")
st.line_chart(data['Volume'])
    
    
    
    
