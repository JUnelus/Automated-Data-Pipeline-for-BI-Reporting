import pandas as pd

def transform_data(df):
    """
    Example transformation: Calculate 7-day moving average for the closing price.
    """
    df['7_day_moving_avg'] = df['Close'].rolling(window=7).mean()
    return df

if __name__ == '__main__':
    df = pd.read_csv('aapl_stock_data.csv')
    transformed_df = transform_data(df)
    transformed_df.to_csv('aapl_stock_data_transformed.csv', index=False)
    print('Data transformed and saved to aapl_stock_data_transformed.csv')
