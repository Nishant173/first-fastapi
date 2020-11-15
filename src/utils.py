import random
import sqlite3
import pandas as pd
import config

def get_sqlite_db_connection(db_name: str) -> sqlite3.Connection:
    """Returns SQLite database connection object, given the name of the database you wish to connect to"""
    connection_obj = sqlite3.connect(database=db_name)
    return connection_obj


def dataframe_to_sports_db(df: pd.DataFrame) -> None:
    df.to_sql(name=config.TBL_SPORTS,
              con=get_sqlite_db_connection(db_name=config.DB_SPORTS),
              if_exists='replace',
              index=False)
    return None


def generate_random_id() -> str:
    """Returns random 12 digit ID (str)"""
    random_id = ""
    characters = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for _ in range(12):
        random_id += random.choice(characters)
    return random_id