from sqlalchemy.orm import Session
import models
import schemas
from sqlalchemy import update
import logging

class PessoaCrud:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_users(self, skip: int, limit: int):
        return self.db.query(models.User).offset(skip).limit(limit).all()

    def get_user(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def get_user_by_email(self, login: str):
        return self.db.query(models.User).filter(models.User.login == login).first()

    def create_user(self, user: schemas.UserCreate):
        db_user = models.User(name=user.name, login=user.login, senha=user.senha)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int ,user: schemas.UserUpdate):
        user.id = user_id
        self.db.query(models.User).filter(
        models.User.id == user_id
        ).update(user.dict())
        self.db.commit()
        return user

    def delete_user(self, user_id: int):
        try:
            db_user = self.db.query(models.User).filter(models.User.id == user_id).first()
            self.db.delete(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            return {"response": "user delected sucessful"}
        except:
            return {"response": "something wrong in query"}
        
    def patch_user(self, user_id: int, user: schemas.UserPatch):
        db_user = self.db.query(models.User).filter(models.User.id == user_id).first()

        for coluna, dado in user.dict(exclude_unset=True).items():
            print(dict(user))
            setattr(db_user, coluna, dado)
        
        self.db.commit()
        self.db.refresh(db_user)
        return user