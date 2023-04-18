from sqlalchemy.orm import Session
import models
import schemas
from sqlalchemy import update
import logging

class PessoaCrud:
    def get_users(self, db: Session, skip: int, limit: int):
        return db.query(models.User).offset(skip).limit(limit).all()

    def get_user(self, db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def get_user_by_email(self, db: Session, login: str):
        return db.query(models.User).filter(models.User.login == login).first()

    def create_user(self, db: Session, user: schemas.UserCreate):
        db_user = models.User(name=user.name, login=user.login, senha=user.senha)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update_user(self, db: Session, user_id: int ,user: schemas.UserUpdate):
        user.id = user_id
        db.query(models.User).filter(
        models.User.id == user_id
        ).update(user.dict())
        db.commit()
        return user

    def delete_user(self, db: Session, user_id: int):
        try:
            db_user = db.query(models.User).filter(models.User.id == user_id).first()
            db.delete(db_user)
            db.commit()
            db.refresh(db_user)
            return {"response": "user delected sucessful"}
        except:
            return {"response": "something wrong in query"}
        
    def patch_user(self, db: Session, user_id: int, user: schemas.UserPatch):
        db_user = db.query(models.User).filter(models.User.id == user_id).first()

        for coluna, dado in user.dict(exclude_unset=True).items():
            print(dict(user))
            setattr(db_user, coluna, dado)
        
        db.commit()
        db.refresh(db_user)
        return user