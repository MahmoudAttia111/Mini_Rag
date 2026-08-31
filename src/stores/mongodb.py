from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

class MongoDBClient:
    client: AsyncIOMotorClient = None

db_client = MongoDBClient()

async def connect_to_mongo():
    settings = get_settings()
    db_client.client = AsyncIOMotorClient(settings.MONGODB_URL)
    print("✅ Connected to MongoDB!")

async def close_mongo_connection():
    db_client.client.close()
    print("✅ MongoDB connection closed!")

def get_db():
    settings = get_settings()
    return db_client.client[settings.MONGODB_DATABASE]
