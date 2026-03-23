import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download stock data
data = yf.download("AAPL", start="2015-01-01")

# Calculate moving averages
data["MA50"] = data["Close"].rolling(window=50).mean()
data["MA200"] = data["Close"].rolling(window=200).mean()

# Create buy/sell signals
data["Signal"] = 0
data.loc[data["MA50"] > data["MA200"], "Signal"] = 1

# Plot
plt.figure()
plt.plot(data["Close"])
plt.plot(data["MA50"])
plt.plot(data["MA200"])
plt.show()