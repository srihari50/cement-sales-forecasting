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
  df = pd.read_excel(data)
  df = df.rename(columns={'Date':'ds', 'Sales_Quantity_Milliontonnes': 'y'})
  df['ds'] = pd.to_datetime(df['ds']) 

  st.write(df)
  train = df.iloc[:84]
  test = df.iloc[84:]
  if train is not None:
     model = Prophet()
     model.fit(train)
     test_df = test.drop(['y'], axis=1)
     test_forecasts = model.predict(test_df)

  test_forecasts = pd.DataFrame(test_forecasts[['yhat', 'yhat_upper', 'yhat_lower']])
  st.write(test_forecasts)

  figure1 = model.plot_components(test_forecasts)
  st.write(figure1)

  figure2 = plot_plotly(model, test_forecasts)
  st.write(figure2)
