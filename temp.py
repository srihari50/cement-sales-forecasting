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

uploaded_file = st.file_uploader(" ", type = ['xlsx'])

if uploaded_file is not None:
	df = pd.read_excel(Uploaded_file)
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
	st.line_chart(data[['Open', 'Close']])

	st.subheader("Volume")
	st.write("Zoom In/Zoom Out for better visualization.")
	st.line_chart(data['Volume'])

	st.header("Prediction")

	def model_np():
		m = pickle.load(open('Prophet.pkl', 'rb'))

		st.subheader("Prophet")
		df = data.copy()
		df.reset_index(inplace=True)
		df_train = df[['Date','Close']]
		df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

		forecast = m.predict(future)
		forecast = forecast.rename(columns={"ds": "Date", "yhat1": "Close"})
		st.write("Forecasting of Etheruem Close Price from 14-09-2021 to 18-09-2021")
		st.write(forecast[['Date', 'Close']].head())
		st.write(f"Forecasting of Close Price of {period} days")
		st.line_chart(forecast['Close'])

	model_np()

