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
     model.add_regressor('GDP_Construction_Rs_Crs')
     model.add_regressor('GDP_Realestate_Rs_Crs')
     model.add_regressor('Oveall_GDP_Growth%')
     model.add_regressor('Water_Source')
     model.add_regressor('Limestone')
     model.add_regressor('Coal_Milliontonne')
     model.add_regressor('Home_Interest_Rate')
     model.add_regressor('Trasportation_Cost')
     model.add_regressor('Order_Quantity_Milliontonnes')
     model.add_regressor('Unit_Price')
     model.fit(train)
     test_df = test.drop(['y'], axis=1)
     test_forecasts = model.predict(test_df)

  test_forecasts = pd.DataFrame(test_forecasts[['yhat', 'yhat_upper', 'yhat_lower', 'Order_Quantity_Milliontonnes']])
  st.write(test_forecasts)

  figure2 = plot_plotly(model, test_forecasts)
  st.write(figure2)
