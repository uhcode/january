from fastapi import FastAPI

from app import app

# Imports API Routes
from routes.LastFM import lastfm

api = FastAPI(
    title="January API",
    description="A fast, secure & open source API for anyone to use.",
    version="0.1.0",
    contact={
        "name": "uhcode",
        "url": "https://t.me/uhcode",
        "email": "hi@january.lol"
    },
)

api.include_router(lastfm)

api.mount('/', app)