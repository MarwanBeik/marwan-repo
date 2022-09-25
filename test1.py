import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")


def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot():
    st.header('GDP per capita in EMEA')
    
    fig = px.bar(df, x='continent', y='gdp_per_capita',
             hover_data=['continent', 'gdp_per_capita'], color='continent',
             height=400)
    
    st.plotly_chart(fig)

def interactive_plot():
    
    x_axis_options = ['gdp_per_capita']
    y_axis_options = ['generosity', 'government_trust', 'happiness_score', 'social_support', 'freedom', 'health']
    x_axis_val = st.selectbox('Select the X-axis', options = x_axis_options)
    y_axis_val = st.selectbox('Select the Y-axis', options = y_axis_options)
    fig2 = px.scatter(df, x=x_axis_val, y=y_axis_val, trendline="ols", color='continent')
    st.plotly_chart(fig2)

st.title('Correlation between Happiness Metrics and GDP')
st.text('This app enables the statistical analysis of World Happiness reports')

st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a World Happiness report')

st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Data Header', 'GDP Distribution', 'Interactive Plots'])


if upload_file is not None:
    df = pd.read_csv(upload_file)


if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'GDP Distribution':
    displayplot()
elif options == 'Interactive Plots':
    interactive_plot()