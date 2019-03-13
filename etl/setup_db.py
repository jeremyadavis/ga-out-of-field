import os
from sqlalchemy import create_engine
# from sqlalchemy.schema import CreateSchema, DropSchema
# from sqlalchemy.sql import exists, select
from utils import pretty_print

DB_URL = os.environ["DATABASE_URL"]


def setup_db():
    try:
        engine = create_engine(DB_URL)
        engine.connect()
        pretty_print(f"Connected to DB at {DB_URL}", True)
        return engine
    except Exception as e:
        print("ERROR! Unable to Connect to database with", DB_URL)
        print(e)
        return False
