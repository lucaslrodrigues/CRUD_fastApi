from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import crud
from schemas import User, UserCreate, UserUpdate, UserPatch
from database import SessionLocal
from app.service.pessoa_service import PessoaService

'''
View

Tem como único trabalho receber os dados vindos da url e retornar uma response

As atividades de regra de negocios ocorrem no service.
O responsavel pelo CRUD é o repository, que se comunica com o BD.
O router atua como um controlador central, redirecionando as entradas para alguma função (o mapa da aplicação)

A aplicação segue o caminho:

    view > service > repository

Quando repository realiza a chamada para a query do crud a aplicação segue o caminho contrario:

    repository > service > repository

    com view retornando uma response no final.

'''

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Este router diferente do @get modifica a url, trazendo um préfixo "/prefixo/users"
@router.get("/users", response_model=List[User])
# As funções de um metodo HTTP são iniciadas com argumentos definidos pelo metodo HTTP,
# sessões do banco e argumentos vindos da request
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Aqui é criada uma instancia da classe PessoaService que recebe a sessão do banco de dados localhost
    # e parametros da query (no caso o inicio e limite de linhas que retornaram no array de dicionario (sera lido como json)) 
    response = PessoaService().get_users(db=db, skip=skip, limit=limit)
    return response

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    response = PessoaService().get_user(db=db, user_id=user_id)
    return response

@router.post("/users", response_model=User)
def save_user(user: UserCreate, db: Session = Depends(get_db)):
    response = PessoaService().save_user(db, user)
    return response

@router.put("/update/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    response = PessoaService().update_user(db=db, user_id=user_id, user=user)
    return response

@router.delete("/delete/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    response = PessoaService().delete_user(db=db, user_id=user_id)
    return response

@router.patch("/patch/{user_id}", response_model = User)
def patch_user(user_id: int, user: UserPatch, db: Session = Depends(get_db)):
    response = PessoaService().patch_user(db=db, user_id=user_id, user=user)
    return response