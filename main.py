from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/post", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, login=user.login)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)



@app.put("/users/update/{id_user}", response_model=schemas.User)
def update_user(id_user: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    # id_exists = crud.get_user_id_exists(db=db, id_user=id_user)
    db_user = crud.update_user(id_user=id_user, db=db, user=user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Algo deu errado")
    return db_user


@app.delete("/users/delete/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    
    id_exists = crud.get_user_id_exists(db, user_id)

    if id_exists is None:
        raise HTTPException(status_code=404, detail="id don't exist")
    
    db_delete = crud.delete_user(db, user_id=user_id)
    
    if db_delete is None:
        raise HTTPException(status_code=404, detail="id doesn't exist")
    raise HTTPException(status_code=200, detail="successfully deleted user")