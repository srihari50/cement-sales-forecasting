import matplotlib.pyplot as plt
import streamlit as st
from datetime import date
import pandas as pd
from PIL import Image
import pickle
import numpy as np
from prophet import Prophet
from prophet.plot import plot_plotly

st.title('Cement Sales Forecasting')

data = st.file_uploader(' ',type='Xlsx')
if data is not None:
  appdata = pd.read_excel(data)
  appdata = appdata.rename(columns={'Sales_Quantity_Milliontonnes': 'y', 'Date':'ds'})
  appdata['ds'] = pd.to_datetime(appdata['ds']) 

  st.write(appdata)
train = df.iloc[:84]
stest = df.iloc[84:]
	

test = test.rename(columns={'Sales_Quantity_Milliontonnes': 'y', 'Date':'ds'})
test_df = test.drop(['y'], axis=1)
test_forecasts = model.predict(test_df)

if test_df is not None:
     obj = Prophet()
     obj.fit(test_df)

test_forecasts = pd.DataFrame(test_forecasts[['yhat', 'yhat_upper', 'yhat_lower', 'Order_Quantity_Milliontonnes']])
st.write(test_forecast)

figure1 = model.plot(test_forecasts)
st.write(figure1)

figure2 = plot_plotly(model, test_forecasts)
st.write(figure2)
