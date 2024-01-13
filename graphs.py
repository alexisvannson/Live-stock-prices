import requests
import json
import yfinance as yf
import matplotlib.pyplot as plt

# Yahoo Finance for historical stock data (AMZN, AAPL, GOOG)
tickers = ["AMZN", "AAPL", "GOOG", "DOW", "GC=F", "MSFT", "TSLA", "NFLX", "NVDA",
            "GOOGL", "IBM", "CSCO", "INTC", "C", "JPM", "BAC", "DIS", "V", 
           "PFE", "MRK", "JNJ", "GS", "XOM", "CVX", "AAP", "KO", "PEP", "WMT", 
           "GS", "BA", "LMT", "GE", "MMM", "CAT", "UNH", "WFC", "VZ", "T", 
           "GS", "CVS","IBM", "CSCO", "INTC", "BABA", "JD", "TCEHY", 
           "AMGN", "GILD", "BIIB", "ABT", "AMAT", "AMD", "MU", "TXN", "COST", 
           "AMAT", "BHP", "RIO", "BP", "GLD", "SLV", "USO", "UNG", "DBA", 
           "JO", "CORN", "WEAT", "SOYB"]

companies = ["Amazon.com Inc.", "Apple Inc.", "Alphabet Inc.", "Dow Inc.", "Gold", 
             "Microsoft Corporation", "Tesla, Inc.", "Netflix, Inc.", "NVIDIA Corporation", 
            "Alphabet Inc. Class A", "International Business Machines Corp.", 
             "Cisco Systems, Inc.", "Intel Corporation", "Citigroup Inc.", "JPMorgan Chase & Co.", 
             "Bank of America Corporation", "The Walt Disney Company", "Visa Inc.", "Pfizer Inc.", 
             "Merck & Co., Inc.", "Johnson & Johnson", "Goldman Sachs Group, Inc.", "Exxon Mobil Corporation", 
             "Chevron Corporation", "Advance Auto Parts, Inc.", "Coca-Cola Company", "PepsiCo, Inc.", 
             "Walmart Inc.", "Goldman Sachs Group, Inc.", "The Boeing Company", "Lockheed Martin Corporation", 
             "General Electric Company", "3M Company", "Caterpillar Inc.", "UnitedHealth Group Incorporated", 
             "Wells Fargo & Co.", "Verizon Communications Inc.", "AT&T Inc.", "Goldman Sachs Group, Inc.", 
             "CVS Health Corporation", "International Business Machines Corp.", 
             "Cisco Systems, Inc.", "Intel Corporation", "Alibaba Group Holding Limited", "JD.com, Inc.", 
             "Tencent Holdings Limited", "Amgen Inc.", "Gilead Sciences, Inc.", "Biogen Inc.", "Abbott Laboratories", 
             "Applied Materials, Inc.", "Advanced Micro Devices, Inc.", "Micron Technology, Inc.", "Texas Instruments Incorporated", 
             "Costco Wholesale Corporation", "Applied Materials, Inc.", "BHP Group Limited", "Rio Tinto Group", 
             "BP p.l.c.", "SPDR Gold Trust", "iShares Silver Trust", "United States Oil Fund, LP", 
             "United States Natural Gas Fund, LP", "Invesco DB Agriculture Fund", "iPath Bloomberg Coffee Subindex Total Return ETN", 
             "Teucrium Corn Fund", "Teucrium Wheat Fund", "Teucrium Soybean Fund"]


yfinance_data = yf.download(tickers, start="2023-01-01", end="2024-01-02")

# Plotting the stock price evolution for each ticker

for i in range(len(tickers)):
    plt.figure(figsize=(10, 5))
    plt.plot(yfinance_data.index, yfinance_data['Close'][tickers[i]])
    plt.title(f'Stock Price Evolution - {companies[i]}') # change that part
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.show()
