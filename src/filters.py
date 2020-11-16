from typing import List, Optional, Union
import crud_ops
import utils

def filter_sports_records(id_: Optional[str] = None,
                          name: Optional[str] = None,
                          name__contains: Optional[str] = None,
                          age: Optional[int] = None,
                          fav_sport: Optional[str] = None,
                          min_age: Optional[int] = None,
                          max_age: Optional[int] = None) -> Union[List[dict], List]:
    """Gets list of records filtered by criteria specified"""
    df = crud_ops.get_sports_records()
    if id_:
        df = df[df['ID'].str.lower() == id_.lower()]
    if name:
        df = df[df['Name'].str.lower() == name.lower()]
    if name__contains:
        name_contained = name__contains.lower()
        df = df[df['Name'].str.lower().str.contains(name_contained)]
    if age:
        df = df[df['Age'] == age]
    if fav_sport:
        df = df[df['FavouriteSport'].str.lower() == fav_sport.lower()]
    if min_age:
        df = df[df['Age'] >= min_age]
    if max_age:
        df = df[df['Age'] <= max_age]
    records = utils.dataframe_to_list(df=df)
    return records