# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 20:40:24 2023

@author: Lenovo
"""

import streamlit as st

from correlation import correlation
from sales_dashboard import Sales_dashboard
from time_Series import time_Series_data
from eda_app import predict_page

st.set_page_config(page_title="Sales Analysis of Tamil Nadu", page_icon=':bar_chart:',layout='wide')
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

page = st.sidebar.selectbox("Breaking down Sales",("Sales Dashboard","Correlation",'Time Series Analysis','Predict'))

if page == 'Sales Dashboard':
     Sales_dashboard()

if page == 'Correlation':
     correlation()
    
if page =='Time Series Analysis':
    time_Series_data()
    
if page == 'Predict':
    predict_page()


    