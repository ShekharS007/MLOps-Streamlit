---

# Stock Market Analysis App 📈  

A simple web application built using [Streamlit](https://streamlit.io/) and [Yahoo Finance API](https://docs.streamlit.io/get-started) to analyze historical stock market data. This app allows users to fetch and visualize stock price data, providing insights such as volume and price trends for various companies.  

## Features  
- Fetch historical stock data for any company.  
- Support for both **Indian** (e.g., RELIANCE.NS, TCS.BO) and **global stocks** (e.g., AAPL, TSLA).  
- Interactive date selection for the analysis period.  
- Visualizations for **stock price (Close)** and **volume** trends.  
- Summary of key metrics like highest, lowest, and average closing prices.  

## Requirements  
Make sure you have the following installed:  
- Python 3.8 or higher  
- Required Python packages:  
  ```bash  
  pip install streamlit pandas numpy yfinance  
  ```  

## Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/ShekharS007/MLOps-Streamlit.git  
   cd stock_market.py  
   ```  

2. Install the required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Run the Streamlit application:  
   ```bash  
   streamlit run stock_market.py  
   ```  

4. Open the application in your browser. By default, it runs at `http://localhost:8501/`.  

## Usage  
1. Enter the **stock ticker symbol** (e.g., `AAPL` for Apple or `RELIANCE.NS` for Reliance Industries Limited on NSE).  
2. Choose the **start date** and **end date** for your analysis.  
3. View the fetched data in tabular format.  
4. Analyze visualizations for stock prices and volume trends.  

> 💡 **Note**:  
> - For **Indian stocks**, append `.NS` (for NSE) or `.BO` (for BSE) to the ticker symbol.  
>   Example: `RELIANCE.NS`, `TCS.BO`.  
> - Ensure the selected date range falls within the stock's trading period.  

## Example Screenshots  

### Input Form:  
![Input Form Screenshot](path-to-image/input-form.png)  

### Stock Data and Visualizations:  
![Visualization Screenshot](path-to-image/visualization.png)  

## Limitations  
- Relies on Yahoo Finance, which might not provide complete data for some symbols.  
- Performance may be slower for large date ranges or low internet speed.  

## Future Improvements  
- Add advanced visualizations using Plotly or Matplotlib.  
- Support for additional financial metrics and indicators.  
- Option to download the fetched data as a CSV file.  
- Real-time stock price updates.  

## Contributing  
Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request.  

## Acknowledgments  
- [Streamlit](https://docs.streamlit.io/get-started) for making interactive web apps easy to build.  
- [Yahoo Finance API](https://pypi.org/project/yfinance/) for providing stock market data.  

---  
