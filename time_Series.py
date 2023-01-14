# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:06:31 2023

@author: Lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import seaborn as sns


@st.cache
def load_data():
    time_df= pd.read_csv(r"C:\Users\Lenovo\Downloads\sales.csv")
    return time_df

time_df = load_data()

def time_Series_data():
   import prophet
    # Converting order_date to datetime datatype
   st.header("Time Series Analysis")
   
   time_df['Order Date'] = pd.to_datetime(time_df['Order Date'])

   time_df['year'] = time_df['Order Date'].apply(lambda x : x.year)
   time_df['month'] = time_df['Order Date'].apply(lambda x : x.month)
   time_df1 = time_df.rename(columns={'Order Date': 'ds', 'Sales': 'y'})
   model = prophet.Prophet()
   model.fit(time_df1)
   future = model.make_future_dataframe(periods=365)
   forecast = model.predict(future)
   
   #yearly prediction
   with st.echo():
    st.write("Yearly Prediction")
    fig1 = model.plot(forecast)
    st.pyplot(fig1)
        

   with st.echo():
       st.header("Plotting Yearly,Seasonal,weekly Trends")
       from prophet.plot import plot_plotly, plot_components_plotly 
       model = prophet.Prophet() 
       model.fit(time_df1)
       forecast = model.predict(time_df1)
       fig = plot_components_plotly(model, forecast)
       st.plotly_chart(fig)
       
       
   
   
   
   
   
   
   
   
    