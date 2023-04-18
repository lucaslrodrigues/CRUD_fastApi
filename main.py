from fastapi import FastAPI
import models
from database import engine
from app.api.router import api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)