import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from routes import base, data
from stores.mongodb import connect_to_mongo, close_mongo_connection

app = FastAPI()

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(base.base_router)
app.include_router(data.data_router)
