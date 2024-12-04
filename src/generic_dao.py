import sqlalchemy
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class GenericDAO:
    def __init__(self, engine):
        self.engine = engine

    def insert_data(self, table_name, data):
        with Session(self.engine) as session:
            try:
                session.execute(
                    sqlalchemy.insert(Table(table_name, MetaData(), autoload_with=self.engine)),
                    [item.__dict__ for item in data]
                )
                session.commit()
                print(f"Successfully inserted data into {table_name}")
            except SQLAlchemyError as e:
                print(f"Error inserting data into {table_name}: {e}")
                session.rollback()

    def process_orders(self):
        with self.engine.connect() as connection:
            try:
                result = connection.execute(sqlalchemy.text("SELECT order_id FROM orders"))
                for row in result:
                    connection.execute(sqlalchemy.text("CALL process_order()"))
                connection.commit()
                print("Successfully processed orders")
            except SQLAlchemyError as e:
                print(f"Error processing orders: {e}")
                connection.rollback()
