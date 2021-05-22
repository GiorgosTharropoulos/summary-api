from fastapi.params import Depends
from app.config import Settings, get_settings
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }
