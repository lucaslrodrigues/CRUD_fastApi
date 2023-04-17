from typing import List
from fastapi import HTTPException
from crud import PessoaCrud

'''
repository

Recebe os dados e os direciona para alguma função do crud.
Seu único trabalho é enviar os dados já tratados 
(é a chamada da chamada de query)

repository.py > crud.py > querybd
'''

class PessoaRepository:
    def __init__(self) -> None:
        self.crud = PessoaCrud()

    def get_users(self, db, skip, limit):
        return self.crud.get_users(db, skip, limit)

    def get_user(self, db, user_id):
        return self.crud.get_user(db, user_id=user_id)

    def get_user_by_login(self, db, login):
        return self.crud.get_user_by_email(db=db, login=login)

    def save_user(self, user, db):
        return self.crud.create_user(db=db, user=user)

    def update_user(self, db, user_id, user):
        return self.crud.update_user(db=db, user_id=user_id, user=user)
    
    def delete_user(self, db, user_id):
        return self.crud.delete_user(db=db, user_id=user_id)
    
    def patch_user(self, db, user_id, user):
        return self.crud.patch_user(db, user_id = user_id, user = user)