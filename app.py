import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de carros en estados unidos')

hist_button = st.button('Build Histogram')
scatter_button = st.button('Build Scatterplot')

if hist_button:
    st.write('Build histogram for vehicle sales dataset')

    fig1 = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig1)

if scatter_button:
    st.write('Building scatterplot for vehicle sales dataset')
    fig2 = px.scatter(car_data, x='price')
    st.plotly_chart()
