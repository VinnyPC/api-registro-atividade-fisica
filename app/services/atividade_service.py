from app.repositories.atividade_repository import AtividadeRepository

class AtividadeService:

    @staticmethod
    def criar_atividade(data):
        return AtividadeRepository.create(data)

    @staticmethod
    def listar_atividades():
        return AtividadeRepository.get_all()

    @staticmethod
    def buscar_por_funcional(funcional):
        return AtividadeRepository.get_by_funcional(funcional)
