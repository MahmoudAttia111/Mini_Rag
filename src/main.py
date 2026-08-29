import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]
    print("✅ Connected to MongoDB!")

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()
    print("✅ MongoDB connection closed!")

app.include_router(base.base_router)
app.include_router(data.data_router)
