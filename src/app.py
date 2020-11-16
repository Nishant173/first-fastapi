from typing import List, Optional, Union
from fastapi import FastAPI
import crud_ops
import filters
import utils

app = FastAPI()

@app.get('/', status_code=200)
def home() -> dict:
    return {"message": "This is the Home page", "status_code": 200}


@app.get('/records', status_code=200)
def get_sports_records() -> Union[List[dict], List]:
    df_records = crud_ops.get_sports_records()
    records = utils.dataframe_to_list(df=df_records)
    return records


@app.get('/record', status_code=200)
def get_sports_record(id_: str) -> dict:
    dict_record = crud_ops.get_sports_record(id_=id_)
    return dict_record


@app.get('/records/filter', status_code=200)
def filter_sports_records(id_: Optional[str] = None,
                          name: Optional[str] = None,
                          age: Optional[int] = None,
                          fav_sport: Optional[str] = None,
                          min_age: Optional[int] = None,
                          max_age: Optional[int] = None) -> Union[List[dict], List]:
    records = filters.filter_sports_records(id_=id_,
                                            name=name,
                                            age=age,
                                            fav_sport=fav_sport,
                                            min_age=min_age,
                                            max_age=max_age)
    return records


@app.put('/record/update', status_code=201)
def update_sports_record(id_: str,
                         name: Optional[str] = None,
                         age: Optional[int] = None,
                         fav_sport: Optional[str] = None) -> dict:
    crud_ops.update_sports_record(id_=id_, name=name, age=age, fav_sport=fav_sport)
    response = {"message": "Record was updated successfully", "status_code": 201}
    return response


@app.post('/record/add', status_code=201)
def add_sports_record(name: str, age: int, fav_sport: str) -> dict:
    crud_ops.add_sports_record(name=name, age=age, fav_sport=fav_sport)
    response = {"message": "Record was added successfully", "status_code": 201}
    return response


@app.delete('/record/delete', status_code=200)
def delete_sports_record(id_: str) -> dict:
    crud_ops.delete_sports_record(id_=id_)
    response = {"message": "Record was deleted successfully", "status_code": 200}
    return response