from typing import Optional
import pandas as pd
import config
import utils

def create_sports_table() -> None:
    conn = utils.get_sqlite_db_connection(db_name=config.DB_SPORTS)
    c = conn.cursor()
    c.execute(f"""
        CREATE TABLE {config.TBL_SPORTS}
        (ID text, Name text, Age int, FavouriteSport text)
    """)
    return None


def get_sports_records(limit: Optional[int] = -1) -> pd.DataFrame:
    """Returns Pandas DataFrame of sports records"""
    if limit > 0:
        query = f""" SELECT * FROM {config.TBL_SPORTS} LIMIT {limit}; """
    else:
        query = f""" SELECT * FROM {config.TBL_SPORTS}; """
    dataframe = pd.read_sql_query(sql=query,
                                  con=utils.get_sqlite_db_connection(db_name=config.DB_SPORTS))
    return dataframe


def get_sports_record(id_: str) -> dict:
    """
    Gets one sports record (dictionary) based on it's ID.
    If the ID given doesn't exist, returns empty dictionary.
    """
    df = get_sports_records()
    df_record = df[df['ID'] == id_]
    if df_record.empty:
        return {}
    if len(df_record) == 1:
        dict_record = df_record.iloc[0].to_dict()
        dict_record['Age'] = int(dict_record['Age'])
        return dict_record
    raise Exception("Multiple records with same ID exists")


def delete_sports_record(id_: str) -> None:
    """
    Deletes one sports record based on it's ID.
    If the ID given doesn't exist, nothing will be deleted.
    """
    df = get_sports_records()
    df_record_to_delete = df[df['ID'] == id_]
    if df_record_to_delete.empty:
        return None
    if len(df_record_to_delete) == 1:
        df_altered = df[df['ID'] != id_]
        utils.dataframe_to_sports_db(df=df_altered)
        return None
    raise Exception("Multiple records with same ID exists")


def add_sports_record(name: str, age: int, fav_sport: str) -> None:
    """Adds one sports record, based on certain parameters given"""
    conn = utils.get_sqlite_db_connection(db_name=config.DB_SPORTS)
    conn.execute(f"""
        INSERT INTO {config.TBL_SPORTS}(ID, Name, Age, FavouriteSport)
        VALUES (?, ?, ?, ?);
    """, (utils.generate_random_id(), name, age, fav_sport))
    conn.commit()
    conn.close()
    return None


def update_sports_record(id_: str,
                         name: Optional[str] = None,
                         age: Optional[int] = None,
                         fav_sport: Optional[str] = None) -> None:
    """Updates one sports record, based on certain parameters given"""
    df = get_sports_records()
    df_record_to_update = df[df['ID'] == id_]
    if df_record_to_update.empty:
        return None
    if len(df_record_to_update) == 1:
        if name:
            df.loc[df['ID'] == id_, 'Name'] = name
        if age:
            df.loc[df['ID'] == id_, 'Age'] = age
        if fav_sport:
            df.loc[df['ID'] == id_, 'FavouriteSport'] = fav_sport
        utils.dataframe_to_sports_db(df=df)
        return None
    raise Exception("Multiple records with same ID exists")