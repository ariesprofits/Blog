import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def calculate_ema(prices, timeframe):
    ema = prices.ewm(span=timeframe, adjust=False).mean()
    return ema

# Download the stock data
ticker = 'AAPL'
data = yf.download(ticker, start="2023-01-01", end="2023-09-12")

# Calculate the 20-day EMA
data['20_day_EMA'] = calculate_ema(data['Close'], 20)

# Plot the closing price and EMA
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label=f'{ticker} Close Price', color='blue', alpha=0.5)
plt.plot(data['20_day_EMA'], label='20-day EMA', color='red', linewidth=2)

# Add title and labels
plt.title(f'{ticker} price and 20-day EMA')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()

plt.show()


ticker = 'GOOGL'
data = yf.download(ticker, start="2023-01-01", end="2023-09-12")


# Calculate the 10-day EMA
data['10_day_EMA'] = calculate_ema(data['Close'], 10)


# Plot the closing price and EMA
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label=f'{ticker} Close Price', color='blue', alpha=0.5)
plt.plot(data['10_day_EMA'], label='10-day EMA', color='red', linewidth=2)


# Add title and labels
plt.title(f'{ticker} price and 10-day EMA')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()


plt.show()