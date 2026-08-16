from fastapi import FastAPI
from dotenv import load_dotenv
from routes.base import base_router

load_dotenv()

app = FastAPI()

app.include_router(base_router, prefix="/api/v1", tags=["api_v1"])
