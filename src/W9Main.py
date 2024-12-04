import os

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import mysql.connector
from dotenv import load_dotenv

load_dotenv(verbose=True)

# Load DataFrames from CSV files
dataframes = {
    'brands': pd.read_csv('../data/brands.csv'),
    'categories': pd.read_csv('../data/categories.csv'),
    'customers': pd.read_csv('../data/customers.csv'),
    'order_items': pd.read_csv('../data/order_items.csv'),
    'orders': pd.read_csv('../data/orders.csv'),
    'products': pd.read_csv('../data/products.csv'),
    'staffs': pd.read_csv('../data/staffs.csv'),
    'stocks': pd.read_csv('../data/stocks.csv'),
    'stores': pd.read_csv('../data/stores.csv'),
}

# Database connection details
db_url = os.getenv('CONNECTION_STRING')
engine = create_engine(db_url, echo=True)

# Loop through DataFrames and write each to the database
for table_name, df in dataframes.items():
    try:
        # Write the DataFrame to the SQL table
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        print(f"Successfully wrote DataFrame to table: {table_name}")
    except Exception as e:
        print(f"Failed to write DataFrame to table: {table_name}. Error: {e}")

df = dataframes['orders']
# Call stored procedure
for index, row in df.iterrows():
    v_order_id = row['order_id']
    cursor = engine.raw_connection().cursor()
    cursor.callproc("process_order", [])
    # cursor.callproc('process_order', [])
    #cursor.commit()
    cursor.close()
