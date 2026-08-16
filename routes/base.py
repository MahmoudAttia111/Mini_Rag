from fastapi import APIRouter
from dotenv import load_dotenv
import os

base_router = APIRouter()

@base_router.get("/")
async def welcome():
    app_name = os.environ.get("APP_NAME", "Mini RAG")
    app_version = os.environ.get("APP_VERSION", "v0.1.0")
    return {
        "app_name": app_name,
        "app_version": app_version
    }
