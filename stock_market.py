import streamlit as st
import pandas as pd
import yfinance as yf

# Set title
st.title("Stock Market Analysis App 📈")

# Introductory text
st.write("""
Analyze stock prices interactively using historical data from Yahoo Finance!
For Indian stocks, use the `.NS` suffix for NSE and `.BO` suffix for BSE. 
Example: `RELIANCE.NS` or `TCS.BO`
""")

# User inputs
ticker_symbol = st.text_input("Enter the stock ticker symbol (e.g. RELIANCE.NS)", "AAPL")
starting_date = st.date_input("Enter the starting date", value=pd.to_datetime("2021-01-01"))
ending_date = st.date_input("Enter the ending date", value=pd.to_datetime("today"))

# Validate date input
if ending_date <= starting_date:
    st.error("Ending date must be later than the starting date.")
else:
    # Load data
    try:
        with st.spinner("Fetching data..."):
            ticker_data = yf.Ticker(ticker_symbol)
            hist = ticker_data.history(start=starting_date, end=ending_date)

        # Check if data is returned
        if hist.empty:
            st.error("No data found for the given ticker symbol and date range.")
        else:
            # Display stock information
            st.subheader(f"Stock Data for {ticker_symbol} from {starting_date} to {ending_date}")
            st.write(hist)

            # Summary statistics
            st.write("### Stock Summary")
            st.write(f"**Highest Closing Price:** ₹{hist['Close'].max():.2f}")
            st.write(f"**Lowest Closing Price:** ₹{hist['Close'].min():.2f}")
            st.write(f"**Average Closing Price:** ₹{hist['Close'].mean():.2f}")

            # Visualizations
            col1, col2 = st.columns(2)
            with col1:
                st.write("### Volume")
                st.line_chart(hist['Volume'])
            with col2:
                st.write("### Closing Price")
                st.line_chart(hist['Close'])

    except Exception as e:
        st.error(f"An error occurred: {e}")
