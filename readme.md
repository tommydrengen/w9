Uge 9 Dataanalyse

    pip install mysql-connector-python

Løsning: W9Main.py

Data læses fra csv-filerne brands, categories, customers, order_items, orders, products, staffs, stocks, stores

Laves til pandas dataframes
Dataframes skrives til sql-tabeller i MySqlDatabasen bikestore vha DataFrame.to_sql()

Stored procedures kaldes fra Python til at hente data vha sqlalchemy
Tabellerne skrives til sql vha pandas dataframe’s to_sql()
Og valideres med print(cursor.fetchall())