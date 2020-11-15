# first-fastapi
My first usage of FastAPI

## Installing dependencies
- Install dependencies with `pip install -r requirements.txt`

## Usage
- Open terminal in the `src` folder.
- Run `uvicorn app:app --reload` to view and explore the available endpoints on your browser.

## Endpoints available
| Endpoint | Description | Example | isIdempotent |
|--|--|--|--|
| `/records` | Gets all records | Self explanatory | True |
| `/records/filter` | Gets records based on some filter parameters | `/records/filter?name=Tony&min_age=18&max_age=51&fav_sport=MMA` | True |
| `/record?id_=SomeId` | Gets one record by ID  | `/record?id_=U0E4CXQSWC4S` | True |
| `/record/add` | Adds record to database | `/record/add?name=Tony&age=37&fav_sport=MMA` | False |
| `/record/update` | Updates record in database. Gets record based on ID, and updates it's other parameters (not all parameters need to be updated) | `/record/update?id_=VN8BB69EU1BV&name=Harrison&age=29&fav_sport=Swimming` | False |
| `/record/delete?id_=SomeId` | Deletes record from the database, based on ID (if the ID exists) | `/quote/delete?id_=KEICNG84DMS7` | True |

## Notes
- I've used a SQLite database.
- The IDs of all the records in the database are automatically randomly generated when new records are created.
- While filtering records, note that the query params are case in-sensitive.