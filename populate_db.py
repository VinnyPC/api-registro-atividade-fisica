#script criado para popular automaticamente o banco de dados em caso de teste

from app.extensions import db_atividades
from app.models.atividade_model import Atividade
from datetime import datetime
from app.repositories.atividade_repository import AtividadeRepository
from loguru import logger
from app import create_app

app = create_app()

def populate():
    try:
        logger.info("Populando banco de dados com dados de teste...")

        atividades_teste = [
        {
        "funcional": "123456",
        "dataHora": "2025-09-24T07:30:00",
        "codigoAtividade": "RUN",
        "descricaoAtividade": "correr 5km"
        },
        {
            "funcional": "654321",
            "dataHora": "2025-09-25T08:00:00",
            "codigoAtividade": "SWIM",
            "descricaoAtividade": "nadar 1km"
        },
        {
            "funcional": "112233",
            "dataHora": "2025-09-26T18:45:00",
            "codigoAtividade": "GYM",
            "descricaoAtividade": "treino de força"
        }
        ]

        with app.app_context():
            for data in atividades_teste:
                AtividadeRepository.create(data)

        logger.success("Banco de dados populado com sucesso!")

    except Exception as e:
        logger.error(f"Erro ao popular banco de dados: {e}", exc_info=True)

if __name__ == "__main__":
    populate()
