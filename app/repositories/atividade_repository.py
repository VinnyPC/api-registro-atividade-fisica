from app.models.atividade_model import Atividade
from app.extensions import db_atividades

class AtividadeRepository:

    @staticmethod
    def create(data):
        atividade = Atividade(**data)
        db_atividades.session.add(atividade)
        db_atividades.session.commit()
        return atividade

    @staticmethod
    def get_all():
        return Atividade.query.all()

    @staticmethod
    def get_by_funcional(funcional):
        return Atividade.query.filter_by(funcional=funcional).all()
