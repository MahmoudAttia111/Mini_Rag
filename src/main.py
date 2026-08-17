import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from routes import base, data

app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)
 