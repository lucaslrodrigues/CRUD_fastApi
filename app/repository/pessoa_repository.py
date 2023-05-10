from typing import List
from fastapi import HTTPException
from crud import PessoaCrud
from sqlalchemy.orm import Session

'''
repository

Recebe os dados e os direciona para alguma função do crud.
Seu único trabalho é enviar os dados já tratados 
(é a chamada da chamada de query)

repository.py > crud.py > querybd
'''

class PessoaRepository:
    def __init__(self, db: Session) -> None:
        self.crud = PessoaCrud(db)

    def get_users(self, skip, limit):
        return self.crud.get_users(skip=skip, limit=limit)

    def get_user(self, user_id):
        return self.crud.get_user(user_id=user_id)

    def get_user_by_login(self, login):
        return self.crud.get_user_by_email(login=login)

    def save_user(self, user):
        return self.crud.create_user(user=user)

    def update_user(self, user_id, user):
        return self.crud.update_user(user_id=user_id, user=user)
    
    def delete_user(self, user_id):
        return self.crud.delete_user(user_id=user_id)
    
    def patch_user(self, user_id, user):
        return self.crud.patch_user(user_id = user_id, user = user)