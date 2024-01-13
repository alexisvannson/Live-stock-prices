import requests
import json
import yfinance as yf
import matplotlib.pyplot as plt
import yfinance as yf
import plotly.graph_objects as go


# Yahoo Finance for historical stock data (AMZN, AAPL, GOOG)
tickers = ["AMZN", "AAPL", "GOOG","MSFT", "TSLA", "NFLX", "NVDA", "JPM"]

companies = ["Amazon.com Inc.", "Apple Inc.", "Alphabet Inc.", "Microsoft Corporation", "Tesla, Inc.", "Netflix, Inc.", "NVIDIA Corporation", "JPMorgan Chase & Co."]


yfinance_data = yf.download(tickers, start="2023-01-01", end="2024-01-02")

# Plotting the stock price evolution for each ticker



for i in range(len(tickers)):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=yfinance_data.index, y=yfinance_data['Close'][tickers[i]], mode='lines', name=f'{companies[i]}'))

    fig.update_layout(
        title=f'Stock Price Evolution - {companies[i]}',
        xaxis_title='Date',
        yaxis_title='Closing Price',
        showlegend=True,
        template="plotly_dark"  # You can choose a different template if needed
    )

    fig.show()


