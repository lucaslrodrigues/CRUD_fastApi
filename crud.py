from sqlalchemy.orm import Session
import models
import schemas
from sqlalchemy import update
import logging

# class crud:
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()

def get_user_id_exists(db: Session, id_user: int):
    return db.query(models.User).filter(models.User.id == id_user).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, login=user.login, senha=user.senha)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def update_user(id_user: int, db: Session, user:schemas.UserUpdate):
#     # logging.info('db_user: ', user)
#     db_user = (
#         update(models.User)
#         .where(models.User.id.in_([id_user]))
#         .values(name=user.name, login=user.login, senha=user.senha)
#     )
#     db.execute(db_user)
#     print(db_user) 

#     return db_user

#     # db_user = models.User(name=user.name, login=user.login, senha=user.senha)
#     # db.add(db_user(id_user=user.id))
#     # db.commit()
#     # db.refresh(db_user)
#     # return db_user

# def update_user(id_user: int, db: Session, user: schemas.UserUpdate):
#     print(models.User.name)
#     db_user = (
#         update(models.User)
#         .where(models.User.id == id_user)
#         .values(name=user.name, login=user.login, senha=user.senha)
#         .returning(models.User)
#     )
#     # print(db_user)
#     # db.execute(db_user)
#     db.commit()
#     # result = db.execute(db_user)
#     # print(result.all())
#     print(db_user)
#     return 

def update_user(id_user: int, db: Session, user: schemas.UserUpdate):
    db.query(models.User).filter(
    models.User.id == id_user
    ).update(models.User)
    db.commit()
    return {'msg': 'passou da query'}

def delete_user(db: Session, user_id: int):
    try:
        db.query(models.User).filter(models.User.id == user_id).delete()
        db.commit()
        return {"msg": "user delected sucessful"}
    except:
        return None