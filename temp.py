import matplotlib.pyplot as plt
import streamlit as st
from datetime import date
import pandas as pd
from PIL import Image
import pickle
import numpy as np
from feature_engine.outliers import Winsorizer
Import pandas_profiling
from prophet import Prophet
from prophet.plot import plot_plotly

st.title('Cement Sales Forecasting')

data = st.file_uploader(' ',type='Xlsx')
if data is not None:
  df = pd.read_excel(data)
  df = df.rename(columns={'Date':'ds', 'Sales_Quantity_Milliontonnes': 'y'})
  df['ds'] = pd.to_datetime(df['ds']) 
  
  from feature_engine.outliers import Winsorizer
  winsor = Winsorizer(capping_method='iqr', tail='both', fold=1.5, variables=['GDP_Construction_Rs_Crs', 'Oveall_GDP_Growth%',
                    'Coal_Milliontonne', 'Home_Interest_Rate'])

  df[['GDP_Realestate_Rs_Crs', 'GDP_Construction_Rs_Crs']] = df[['GDP_Realestate_Rs_Crs', 'GDP_Construction_Rs_Crs']].astype(float)
  
  df[['GDP_Construction_Rs_Crs', 'Oveall_GDP_Growth%', 'Coal_Milliontonne', 'Home_Interest_Rate']] = winsor.fit_transform(df[['GDP_Construction_Rs_Crs',
                                                                          'Oveall_GDP_Growth%', 'Coal_Milliontonne', 'Home_Interest_Rate']])
  
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
     model.add_regressor('Order_Quantity_Milliontonnes')
     model.add_regressor('Trasportation_Cost')
     model.add_regressor('Unit_Price')
     model.fit(train)
     test_df = test.drop(['y'], axis=1)
  if test_df is not None:
     test_forecasts = model.predict(test_df)

  forecasts = pd.DataFrame(test_forecasts[['ds', 'yhat', 'yhat_upper', 'yhat_lower']])
  forecasts = forecasts.tail(12)
  st.header('Forecasts')
  st.write(forecasts)

figure1 = model.plot(test_forecasts)
st.write(figure1)

figure2 = plot_plotly(model, test_forecasts)
st.write(figure2)
