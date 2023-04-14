from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
import models
from schemas import User, UserCreate, UserUpdate, UserPatch
from database import SessionLocal, engine
from app.api.router import api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)