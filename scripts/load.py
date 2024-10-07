import sqlalchemy as db
import pandas as pd


def load_data_to_redshift(file_path, redshift_config):
    engine = db.create_engine(
        f"postgresql://{redshift_config['redshift_user']}:{redshift_config['redshift_password']}@{redshift_config['redshift_host']}/{redshift_config['redshift_db']}")
    df = pd.read_csv(file_path)

    with engine.connect() as conn:
        df.to_sql('financial_data', conn, if_exists='replace', index=False)


if __name__ == '__main__':
    config = {
        'redshift_user': 'admin',
        'redshift_password': 'LSKXWjkefl834&(',
        'redshift_host': 'redshift-cluster-endpoint',
        'redshift_db': 'mydb'
    }
    load_data_to_redshift('transformed_data.csv', config)
