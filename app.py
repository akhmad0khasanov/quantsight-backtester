# Write code yourself, not AI
import streamlit as st 
import plotly as pl
import datetime as datetime

# Stocks and fForex
import yfinance as yf

# Crypto
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

st.title('QuantSight Backtester')

# Asset selection method
def hist_data():

    option = st.selectbox('Upload csv', 'Select Asset')

    # Inputing manually
    if option == 'Upload csv':
        file = st.file_uploader('Drag and drop or select file')
        # logic
        

    elif option == 'Select Asset':
        asset = st.selectbox('Stocks', 'Crypto', 'Forex')

        # stocks
        if asset == 'Stocks':
            stock_ticker = st.text_input('Select a ticker', value = 'AAPL')
            stock_start_date = st.text_input('Start date', value = 'YYYY-MM-DD')
            stock_end_date = st.text_input('Ends date', value = 'YYYY-MM-DD')

            # logic
            a_start_date = datetime.strptime(stock_start_date, '%Y-%m-%d')
            a_end_date = datetime.strptime(stock_end_date, '%Y-%m-%d')

            ticker = yf.Ticker(stock_ticker)
            stock_data = ticker.history(start = a_start_date, end = a_end_date)


        # crypto
        elif asset == 'Crypto':
            coin_id = st.text_input('Coin ID', value = 'bitcoin')
            vs_currency = st.text_input('Select currency', value = 'usd')
            days = st.text_input('Number of days', value = 'max')

            crypto_data = cg.get_coin_market_chart_by_id(id=coin_id, vs_currency=vs_currency, days=days)


        # forex
        elif asset == 'Forex':
            forex_pair = st.text_input('Select a ticker', value = 'EURUSD=X')
            forex_start_date = st.text_input('Start date', value = 'YYYY-MM-DD')
            forex_end_date = st.text_input('Ends date', value = 'YYYY-MM-DD')

            # logic
            adjusted_start_date = datetime.strptime(forex_start_date, '%Y-%m-%d')
            adjusted_end_date = datetime.strptime(forex_end_date, '%Y-%m-%d')

            yf_forex_ticker = yf.ticker(forex_pair)
            forex_data = ticker.history(yf_forex_ticker, start = adjusted_start_date, end = adjusted_end_date)


