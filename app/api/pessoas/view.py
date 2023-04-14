from typing import List
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
import crud
import models
from schemas import User, UserCreate, UserUpdate, UserPatch
from database import SessionLocal, engine
from app.service.pessoa_service import PessoaService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    response = PessoaService().save_service(db, user)
    return response



@router.put("/users/update/{id_user}", response_model=User)
def update_user(id_user: int, user: UserUpdate, db: Session = Depends(get_db)):
    # id_exists = crud.get_user_id_exists(db=db, id_user=id_user)
    db_user = crud.update_user(id_user=id_user, db=db, user=user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Algo deu errado")
    raise HTTPException(status_code=200, detail="successfully update user")


@router.delete("/users/delete/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    
    id_exists = crud.get_user_id_exists(db, user_id)

    if id_exists is None:
        raise HTTPException(status_code=404, detail="id don't exist")
    
    db_delete = crud.delete_user(db, user_id=user_id)
    
    if db_delete is None:
        raise HTTPException(status_code=404, detail="id doesn't exist")
    raise HTTPException(status_code=200, detail="successfully deleted user")

@router.patch("/users/patch/{id_user}", response_model = User)
def patch_user(id_user: int, user: UserPatch, db: Session = Depends(get_db)):

    db_user = crud.patch_user(db, id_user = id_user, user = user)

    if db_user is None:
        raise HTTPException(status_code=404, detail="not found")
    raise HTTPException(status_code=200, detail="successfully update user")