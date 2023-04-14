from typing import List
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
import crud
import models
from schemas import User, UserCreate, UserUpdate, UserPatch
from database import SessionLocal, engine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/numero")
def read_users():
    return {"msg": "ok"}
