import yfinance as yf
import pandas as pd

# Function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(start=start_date, end=end_date)
    return stock_data

# Function to calculate moving average
def moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

# Main program
if __name__ == "__main__":
    ticker = input("Enter stock ticker: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Fetch stock data
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    print("\nStock data:\n", stock_data.head())

    # Calculate moving averages
    stock_data['MA_10'] = moving_average(stock_data, 10)
    stock_data['MA_50'] = moving_average(stock_data, 50)

    print("\nStock data with moving averages:\n", stock_data.tail())

    # Basic analysis
    latest_close = stock_data.iloc[-1]['Close']
    ma_10 = stock_data.iloc[-1]['MA_10']
    ma_50 = stock_data.iloc[-1]['MA_50']

    print(f"\nLatest close price: {latest_close:.2f}")
    print(f"10-day moving average: {ma_10:.2f}")
    print(f"50-day moving average: {ma_50:.2f}")

    if ma_10 > ma_50:
        print("\nThe 10-day moving average is above the 50-day moving average. This may be a bullish signal.")
    elif ma_10 < ma_50:
        print("\nThe 10-day moving average is below the 50-day moving average. This may be a bearish signal.")
    else:
        print("\nThe 10-day and 50-day moving averages are the same. This may indicate a neutral trend.")
