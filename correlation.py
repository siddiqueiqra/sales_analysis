# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 17:50:42 2023

@author: Lenovo
"""
import pandas as pd
import plotly.express as px
import streamlit as st


def load_data():
       new_df = pd.read_csv(r"C:\Users\Lenovo\Downloads\sales.csv")
       return new_df
   
new_df = load_data()
def correlation():   
       st.header("Finding Correlation between variables")
       new_df = pd.read_csv(r"C:\Users\Lenovo\Downloads\sales.csv")
       contingency_table =pd.crosstab(new_df['Category'],new_df['Sub Category'],margins =False)
       fig = px.imshow(contingency_table)
       st.subheader("Correlation between sub-category and category")
       st.plotly_chart(fig)
       st.markdown("*Inference*")
       st.write("- *Bevarages has highest correlation with Health Drinks with 719 frequencies and with soft drinks 619 frequencies* ")
       st.write("- *Sub-category like health drinks and soft drinks has highest correlation with bevarage category* ")
           
       contingency_table2=pd.crosstab(new_df['Category'],new_df['City'],margins =False)
       fig1 = px.imshow(contingency_table2)
       st.subheader("Correlation between category and city")
       st.plotly_chart(fig1)
       st.markdown(" *Inference*" )
       st.write (" - *for bakery cities like krishnagiri and salem has highest frequencies*")
       st.write("- *for Beverages cities like Madurai and perambalur has highest frequencies of sales* ")
       st.write("- *for Egg-meat and fish cities like karur,kanyakumari krishnagri, cumbum have highest frequencies* ")
       st.write("- *for foodgrains cities like bodi,kanyakumari ,krishnagri, ooty have highest frequencies* ")
       st.write("- *for Fruits and veggies cities like bodi, coimbatore, nagercoil, pudukottia,tirunelveli , virudhu have highest frequencies* ")
       st.write("- *for oil and masala cities like kanyakumari ,salem and pudukottia have highest frequencies* ")
       st.write("- *for snacks cities like kanyakumari ,perambalur ,tirunelveli and virudhuhave highest frequencies* ")

       contingency_table4 = pd.crosstab(new_df['Category'],new_df['Region'],margins=False)
       fig2 = px.imshow(contingency_table4)
       st.subheader("Correlation between category and region")
       st.plotly_chart(fig2)
       st.write("Inference")
       st.write("- *West hase highest correlation with every category* ")
     