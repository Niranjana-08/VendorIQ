import os
import pandas as pd
from sqlalchemy import create_engine
import logging
import time

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Only call basicConfig ONCE, at the start
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''this fn will ingest the dataframe into database table'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_raw_data():
    '''this fn will load the csvs as dataframes and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/' + file)
            logging.info(f'Ingesting {file} in db')  # This is fine
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end-start)/60
    logging.info('Ingestion Complete')    
    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()
