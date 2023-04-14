from typing import List
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
import crud
import models
from schemas import User, UserCreate, UserUpdate, UserPatch
from database import SessionLocal, engine

class PessoaRepository:
    def save_repository(self, user, db):
        db_user = crud.get_user_by_email(db, login=user.login)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return crud.create_user(db=db, user=user)