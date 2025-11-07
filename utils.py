import os
import sqlalchemy
import pandas as pd

def check_uniqueness(df):
    unique_columns = {col: df[col].is_unique for col in df.columns}
    for col, is_unique in unique_columns.items():
        print(f"{col}: {'Unique' if is_unique else 'Not unique'}")


# This returns an SQLAlchemy engine. Which is an object that manages the connection to a database. This handles
# talking to the database, sending SQL queries and returning results
def get_engine():
    username = os.getenv("SQL_USER")
    password = os.getenv("SQL_PASSWORD")
    server = os.getenv("SQL_SERVER")
    database = os.getenv("SQL_DATABASE")

    connection_string = (
        f"mssql+pyodbc://{username}:{password}@{server}/{database}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    engine = sqlalchemy.create_engine(connection_string)
    return engine

def read_table(table_name: str) -> pd.DataFrame:

    engine = get_engine()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    return df