from app.repository.pessoa_repository import PessoaRepository
from fastapi import HTTPException
from sqlalchemy.orm import Session
'''
Neste arquivo temos a regra de negocios

caso eu queira executar algum tratamento de dados, está é a pasta para isso

exemplo de tratamento:
    Posso ter a regra de que todos os nomes devem estar em upper case,
    então posso modificar o testo nome e enviar para o repository

        user.name = upper(user.name)

    Também posso verificar se é um valor null

        return {"400": "failed to read username"} if user.name is none else {"200": "ok"}

    Posso delimitar que caso o retorno seja vazio retorne uma exception de erro
'''

class PessoaService:
    def __init__(self, db: Session) -> None:
        self.pessoa_repository = PessoaRepository(db)
        self.db = db
    
    def get_users(self, skip, limit):
        response = self.pessoa_repository.get_users(skip=skip, limit=limit)
        return {"response": "empty table"} if len(response) == 0 else response
    
    def get_user(self, user_id):
        response = self.pessoa_repository.get_user(user_id=user_id)
        if response is None:
            raise HTTPException(status_code=404, detail={"response": "User not found"})
        return response

    def save_user(self, user):
        response = self.pessoa_repository.get_user_by_login(login=user.login)

        if response:
            raise HTTPException(status_code=400, detail={"response": "Email already registered"})
        else:
            response = self.pessoa_repository.save_user(user=user)
        return response
    
    def update_user(self, user_id, user):
        response = self.pessoa_repository.get_user(user_id=user_id)
        response = {"404": "user not found"}  if response is None else self.pessoa_repository.update_user(user_id=user_id, user=user)
        return response
    
    def delete_user(self, user_id):
        response = self.pessoa_repository.get_user(user_id=user_id)
        response = {"response": "user not found"} if response is None else self.pessoa_repository.delete_user(user_id=user_id)
        return response

    def patch_user(self, user_id, user):
        response = self.pessoa_repository.get_user(user_id=user_id)
        response = {"response": "user not found"} if response is None else self.pessoa_repository.patch_user(user_id=user_id, user=user)
        return response
