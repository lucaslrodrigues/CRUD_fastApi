from fastapi.routing import APIRouter
from app.api.pessoas import view
from app.api.enderecos import view as endereco_view

'''
router

Direciona as solicitações HTTP recebidas para as funções correspondentes
Ele utiliza dos metodos: HTTP, URL e parametros de solicitação
Isso faz com que a url não precise ser alterada em cada função
'''

api_router = APIRouter()

# Aqui estou dizendo que o que vier de view estará na url .../pessoas
# Ex: .../pessoas/usuario
api_router.include_router(view.router, prefix="/pessoas", tags=["pessoas"])

api_router.include_router(endereco_view.router, prefix="/pessoas", tags=["pessoas"])
