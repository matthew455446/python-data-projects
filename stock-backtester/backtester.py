import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download stock data
data = yf.download("AAPL", start="2015-01-01")

# Moving averages
data["MA50"] = data["Close"].rolling(window=50).mean()
data["MA200"] = data["Close"].rolling(window=200).mean()

# Trading signal
data["Signal"] = 0
data.loc[data["MA50"] > data["MA200"], "Signal"] = 1

# Daily returns
data["Market Return"] = data["Close"].pct_change()

# Strategy returns
data["Strategy Return"] = (
    data["Market Return"] * data["Signal"].shift(1)
)

# Cumulative returns
data["Market Growth"] = (
    1 + data["Market Return"]
).cumprod()

data["Strategy Growth"] = (
    1 + data["Strategy Return"]
).cumprod()

# Print results
print("Final Market Return:",
      data["Market Growth"].iloc[-1])

print("Final Strategy Return:",
      data["Strategy Growth"].iloc[-1])

# Plot performance
plt.figure()

plt.plot(data["Market Growth"])
plt.plot(data["Strategy Growth"])

plt.title("Strategy vs Buy and Hold")
plt.xlabel("Date")
plt.ylabel("Growth")

plt.show()