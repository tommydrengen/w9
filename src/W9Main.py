import os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Import your new classes
from generic_dto import GenericDTO
from generic_dao import GenericDAO

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

# Create GenericDAO instance
dao = GenericDAO(engine)

# Loop through DataFrames and write each to the database
for table_name, df in dataframes.items():
    try:
        # Convert DataFrame to list of GenericDTOs
        data = [GenericDTO(**row) for row in df.to_dict('records')]  ## TODO GenericDTO's init need to take **row as inpart arguments

        # Insert data using dao
        dao.insert_data(table_name, data)
    except Exception as e:
        print(f"Failed to write DataFrame to table: {table_name}. Error: {e}")

# Process orders
res = dao.process_orders()
print("res:")
print(res)
print("res slut")

