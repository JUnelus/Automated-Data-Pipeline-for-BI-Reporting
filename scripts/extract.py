import boto3
import pandas as pd
import yfinance as yf


def upload_data_to_s3(file_path, bucket, key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket, key)


def get_stock_data(symbol, period='1mo', interval='1d'):
    """
    Fetches stock data using Yahoo Finance API.

    :param symbol: Stock ticker symbol (e.g., 'AAPL' for Apple Inc.)
    :param period: Data period ('1d', '5d', '1mo', '3mo', '1y', '5y', 'max')
    :param interval: Data interval ('1d', '1wk', '1mo')
    :return: Pandas DataFrame containing stock price data
    """
    stock_data = yf.download(symbol, period=period, interval=interval)
    return stock_data


def save_to_csv(df, file_path):
    """
    Saves the DataFrame to a CSV file.

    :param df: Pandas DataFrame containing the stock data.
    :param file_path: Path to save the CSV file.
    """
    df.to_csv(file_path, index=True)
    upload_data_to_s3(file_path, 'my-data-bucket1', 'financial-data/aapl_stock_data.csv')
    print(f'Data saved to {file_path}')


if __name__ == '__main__':
    # Example stock symbol: Apple Inc. ('AAPL')
    symbol = 'AAPL'
    stock_data = get_stock_data(symbol, period='1mo', interval='1d')

    # Save to CSV
    save_to_csv(stock_data, 'aapl_stock_data.csv')
