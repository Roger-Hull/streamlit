import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

header = st.container()
features = st.container()
run = st.container()
dataset = st.container()
modelTraining = st.container()


with st.sidebar:
    st.sidebar.button('Analysis Tool')
    st.sidebar.button('Methodology')

with header:
    st.title('Technical and Sentiment Stock Trading Algorithm')
    st.write('This web application is designed to help retail stock traders and investors determine if they should buy or sell a stock using news sentiment analysis and technical stock trading analysis. If you wish to learn more about our methodology, please visit the methodology tab')
    
with features:
    st.subheader('Select Your Features')
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.write("Date Range")
        
    with col2:
        if st.checkbox('Use NYT Sentiment Analysis?'):
            st.write('Sentiment Analysis has been added to the chart')
        
    with col3:
        st.write("EMA Window")
        st.slider('Days',0,60,5) #min: 0, max:60, def:5
        
    with col4:
        st.write('SMA Window')
        st.slider('Days',0,180,40) #min: 0, max:180, def:40
        
    with col5:
        option = st.selectbox(
        'Select your trading strategy',
        ('MACD','SVM'))
        st.write('You selected:',option)
        
with run:
    st.button('Run My Trading Algoritm')

with dataset:
    df = pd.read_csv('aapl.csv')
    st.line_chart(data=df['close'], width=0, height=0, use_container_width=True)