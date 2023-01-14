# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:39:48 2023

@author: Lenovo
"""

# sales dashboard

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import seaborn as sns


@st.cache
def load_data():
    df=pd.read_csv(r"C:\Users\Lenovo\Downloads\new_data.csv")
    return df

df=load_data()  

def calculate_total_sales(sales_data):
    total_sales = df['Sales'].sum()
    return total_sales

def Sales_dashboard():        
       st.title(":bar_chart: Sales Dashboard")
       st.markdown("##")
   # ---- SIDEBAR ----
       st.sidebar.subheader("Please Filter Here:")
   #city = st.sidebar.multiselect("Select the City:",options=df["City"].unique())
       category_type = st.sidebar.multiselect("Select the Category:", 
                                              options=df["Category"].unique(),
                                              default=df["Category"].unique())
       region_type = st.sidebar.multiselect("Select the Region:",
                                              options=df["Region"].unique(),
                                               default=df['Region'].unique()
                                            )

       df_selection = df.query(
              "Category ==@category_type & Region == @region_type")
   

       Total_sales = int(df_selection['Sales'].sum())
       Total_profit = int(df_selection['Profit'].sum())
   
       st.write("Showing Results Based on Filter:")
       left_column, middle_column, right_column= st.columns(3)
       with left_column:
            st.subheader("Total Sales:")
            st.subheader(f"Rs {Total_sales:,}")
       with middle_column:
            st.subheader("Total Profit:")
            st.subheader(f"Rs {Total_profit:,}")            
       with right_column:
            st.subheader("Profit margin:")
            profit_margin = Total_profit / Total_sales
            st.subheader(f"{profit_margin:.2%}")
       st.markdown("""---""")
            
       sales_by_product_line = (
            df_selection.groupby(by=["Category"]).sum()[["Sales"]].sort_values(by="Sales")
)
       fig_product_sales = px.bar(
          sales_by_product_line,
               x="Sales",
               y=sales_by_product_line.index,
               orientation="h",
               title="<b>Sales by Product Line</b>",
               color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
               template="plotly_white",
)
       fig_product_sales.update_layout(
             plot_bgcolor="rgba(0,0,0,0)",
             xaxis=(dict(showgrid=False))
)    
       profit_by_region = df_selection.groupby(by=["Region"]).sum()[["Profit"]]
       regionly_profit = px.bar(
       profit_by_region,
       x=profit_by_region.index,
       y="Profit",
       title="<b>Profit by region by </b>",
       color_discrete_sequence=["#0083B8"] * len(profit_by_region),
       template="plotly_white",
)
       regionly_profit.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

       left_column, right_column = st.columns(2)
       left_column.plotly_chart(regionly_profit, use_container_width=True)
       right_column.plotly_chart(fig_product_sales, use_container_width=True)
   
       st.subheader("Click on buttons to see visuals")
       if st.button('Show yearly Profit'):
             chart2= st.bar_chart(df.groupby('year')['Profit'].sum())
       if st.button('Show City Sales Chart'):
             chart = st.bar_chart(df.groupby('City')['Sales'].sum().sort_index(ascending=False))
       if st.button('Show sub-Category Sales'):
             chart1 = st.bar_chart(df.groupby('Sub Category')['Sales'].sum().sort_index(ascending=False)) 
       st.markdown("""---""")
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
 
