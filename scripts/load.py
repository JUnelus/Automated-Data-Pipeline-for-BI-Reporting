import os
import sqlalchemy as db
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def load_data_to_postgres(file_path):
    engine = db.create_engine(
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}")
    df = pd.read_csv(file_path)

    with engine.connect() as conn:
        df.to_sql('apple_financial_data', conn, if_exists='replace', index=False)


if __name__ == '__main__':
    load_data_to_postgres('C:/Users/big_j/PycharmProjects/Automated-Data-Pipeline-for-BI-Reporting/scripts/aapl_stock_data_transformed.csv')
