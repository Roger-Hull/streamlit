import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Streamlit's layout is configured with contrainers (rows) and columns. The columns are nested withing the rows. The pages, such as our methodology page, must be held within a pages directory. Then, when we run the analysis tool using the "streamlit run analysis_tool.py" in our terminal, streamlit will look for the pages directory and add in any python files included.

# These are our containers.
header = st.container()
features = st.container()
run = st.container()
dataset = st.container()
results = st.container()

#Calling the header container.

with header:
    st.title('Technical and Sentiment Stock Trading Algorithm')
    st.write('This web application is designed to help retail stock traders and investors determine if they should buy or sell a stock using news sentiment analysis and technical stock trading analysis. If you wish to learn more about our methodology, please visit the methodology tab')
    
# Calling the features container
with features:
    with st.form('Select Your Features'):
        ticker = st.selectbox(
            'Select your index',
            ('NASDAQ','S&P 500','RUSSEL')
        )
        
        date = st.selectbox(
            'Date Range',
            ('Dot Com Bubble',
             '2008 Crash',
             'Covid')
        )
        
        nlp = st.checkbox('Use NYT Sentiment Analysis?')
        
        trading_options = ['MACD','SVM']
        strategy = st.radio(
            'Select your trading strategy',
            trading_options
        )
        if strategy == 'MACD':
            ema = st.slider('Days',0,60,5) #min: 0, max:60, def:5
            sma = st.slider('Days',0,180,40) #min: 0, max:180, def:4
        elif strategy == 'SVM':
            pass
    
        submitted = st.form_submit_button('Run My Algorithm')
        if submitted:
            st.write(ticker, date, nlp, strategy)
    
    
with run:
    df = pd.read_csv(ticker)
    

with dataset:
    df = pd.read_csv('aapl.csv')
    st.line_chart(
        data=df['close'], 
        width=0, 
        height=0, 
        use_container_width=True
        )

#Calling the resutls container    

with results:
    st.header('Trading Algorithm Results')
    col6, col7, col8, col9 = st.columns(4)
              
    with col6:
              st.write('Cumulative Return')
              st.write("")
    with col7:
              st.write('Volatility')
              st.write("")
    with col8:
              st.write('Sharpe Ratio')
              st.write('')
    with col9:
              st.write('Sortino Ratio')
              st.write('')