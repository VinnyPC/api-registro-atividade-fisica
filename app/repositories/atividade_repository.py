from app.models.atividade_model import Atividade
from app.extensions import db_atividades
from loguru import logger

class AtividadeRepository:

    @staticmethod
    def create(data):
        try:
            atividade = Atividade(**data)
            db_atividades.session.add(atividade)
            db_atividades.session.commit()
            logger.info(f"Atividade gravada: {atividade.id}")
            return atividade
        except Exception as e:
            db_atividades.session.rollback()
            logger.error(f"Erro ao gravar atividade: {e}", exc_info=True)
            raise

    @staticmethod
    def get_all():
        return Atividade.query.all()

    @staticmethod
    def get_by_funcional(funcional):
        return Atividade.query.filter_by(funcional=funcional).all()
    
    @staticmethod
    def get_paginated_and_filtered(page=1, per_page=10, filters=None):
        query = Atividade.query

        if filters:
            if "tipo" in filters:
                query = query.filter(Atividade.tipo == filters["tipo"])
            if "data_inicio" in filters and "data_fim" in filters:
                query = query.filter(
                    Atividade.data.between(filters["data_inicio"], filters["data_fim"])
                )


        pagination = query.paginate(page=page, per_page=per_page, error_out=False)

        return {
            "items": [atividade.to_dict() for atividade in pagination.items],
            "total": pagination.total,
            "page": pagination.page,
            "pages": pagination.pages,
            "per_page": pagination.per_page
        }
