from app.repository.pessoa_repository import PessoaRepository

class PessoaService:
    def __init__(self) -> None:
        self.pessoa_repository = PessoaRepository()
     
    def save_service(self, db, user):
        user.name = user.name + "Banana"
        response = self.pessoa_repository.save_repository(db=db, user=user)
        return response
