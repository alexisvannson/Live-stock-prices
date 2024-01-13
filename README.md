# Live-stock-prices
The script takes data from the yahoo finance api and generates graphs representing this data

Certainly! Let's break down the code step by step:

1. **Imports:**
   ```python
   import yfinance as yf
   import plotly.graph_objects as go
   ```
   - The script fetches financial data from Yahoo Finance (`yfinance`), and creating interactive plots (`plotly`).

2. **Stock Tickers and Company Names:**
   ```python
   tickers = ["AMZN", "AAPL", "GOOG", "MSFT", "TSLA", "NFLX", "NVDA", "JPM"]
   companies = ["Amazon.com Inc.", "Apple Inc.", "Alphabet Inc.", "Microsoft Corporation", "Tesla, Inc.", "Netflix, Inc.", "NVIDIA Corporation", "JPMorgan Chase & Co."]
   ```
   - Two lists are defined: `tickers` contains the stock symbols for the selected companies, and `companies` contains their corresponding names.

3. **Fetch Historical Stock Data:**
   ```python
   yfinance_data = yf.download(tickers, start="2023-01-01", end="2024-01-02")
   ```
   - The `yfinance.download` function is used to fetch historical stock data for the specified tickers within the date range from January 1, 2023, to January 2, 2024.

4. **Plotting Stock Price Evolution:**
   ```python
   for i in range(len(tickers)):
       fig = go.Figure()
       fig.add_trace(go.Scatter(x=yfinance_data.index, y=yfinance_data['Close'][tickers[i]], mode='lines', name=f'{companies[i]}'))
       fig.update_layout(
           title=f'Stock Price Evolution - {companies[i]}',
           xaxis_title='Date',
           yaxis_title='Closing Price',
           showlegend=True,
           template="plotly_dark"
       )
       fig.show()
   ```
   - A loop iterates through each stock ticker.
   - A Plotly `Figure` is created for each company, and a scatter plot is added with dates on the x-axis and closing prices on the y-axis.
   - The layout is customized with a title, axis labels, and a dark template.
   - The resulting plot is displayed.

5. **Note:**
   - The script utilizes the Plotly library for interactive and visually appealing plots.

6. **Customization:**
   - You can customize the script by adjusting the tickers, companies, date range, and plot layout to suit your analysis needs.

The script fetches historical stock data, creates individual plots for each company's stock price evolution, and displays them using Plotly.
