from fastapi.routing import APIRouter
from app.api.pessoas import view
from app.api.enderecos import view as endereco_view

api_router = APIRouter()
api_router.include_router(view.router, prefix="/pessoas", tags=["pessoas"])
api_router.include_router(endereco_view.router, prefix="/pessoas", tags=["pessoas"])
