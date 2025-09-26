from app.repositories.atividade_repository import AtividadeRepository
from datetime import datetime
from flask import jsonify

class AtividadeService:
    REQUIRED_FIELDS = [
        "funcional", "nome", "descricao", "tipo",
        "duracao", "distancia", "intensidade", "data", "calorias"
    ]
    @staticmethod
    def criar_atividade(data: dict):
        extra_fields = set(data.keys()) - set(AtividadeService.REQUIRED_FIELDS)
        missing_fields = set(AtividadeService.REQUIRED_FIELDS) - set(data.keys())
        if extra_fields:
            raise ValueError(f"Campos não permitidos: {extra_fields}")
        if missing_fields:
            raise ValueError(f"Campos obrigatórios faltando: {missing_fields}")


        try:
            data_convertida = datetime.strptime(data["data"], "%d-%m-%Y").date()
            data["data"] = data_convertida
        except ValueError:
            return jsonify({"error": "Data deve estar no formato DD/MM/AAAA"}), 400

        #validando tipos de dados básicos
        if not isinstance(data["funcional"], str) or len(data["funcional"]) > 50:
            raise ValueError("Campo 'funcional' inválido")
        if not isinstance(data["nome"], str) or len(data["nome"]) > 100:
            raise ValueError("Campo 'nome' inválido")
        if data.get("tipo") and not isinstance(data["tipo"], str):
            raise ValueError("Campo 'tipo' inválido")
        if data.get("duracao") and not isinstance(data["duracao"], int):
            raise ValueError("Campo 'duracao' inválido")
        if data.get("distancia") and not isinstance(data["distancia"], (int, float)):
            raise ValueError("Campo 'distancia' inválido")
        if data.get("intensidade") and not isinstance(data["intensidade"], str):
            raise ValueError("Campo 'intensidade' inválido")
        if data.get("calorias") and not isinstance(data["calorias"], int):
            raise ValueError("Campo 'calorias' inválido")

        return AtividadeRepository.create(data)

    @staticmethod
    def listar_atividades():
        return AtividadeRepository.get_all()

    @staticmethod
    def buscar_por_funcional(funcional):
        return AtividadeRepository.get_by_funcional(funcional)
