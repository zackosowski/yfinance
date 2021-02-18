import yfinance as yf

tesla = yf.Ticker("TSLA")
print(tesla.info)