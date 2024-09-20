from fastapi import FastAPI

from app import app

api = FastAPI()

api.mount('/', app)