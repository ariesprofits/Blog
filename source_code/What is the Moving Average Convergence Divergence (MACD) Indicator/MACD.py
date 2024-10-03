import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = 'AAPL' # define ticker symbol

# pull in price data from yfinance
data = yf.download(ticker, "2020-01-01", "2020-12-31")
df = pd.DataFrame(data)

# 26-period EMA
df['EMA26'] = df['Close'].ewm(span=26,adjust=False).mean()
# 12-period EMA
df['EMA12'] = df['Close'].ewm(span=12,adjust=False).mean()
# MACD line
df['MACD'] = df['EMA12'] - df['EMA26']
# Signal line
df['Signal'] = df['MACD'].ewm(span=9,adjust=False).mean()

# Plot MACD
plt.Figure(figsize=(40,44))
plt.plot(df["Close"])
plt.plot(df['Signal'])
plt.plot(df['MACD'])