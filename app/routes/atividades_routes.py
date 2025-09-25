from flask import Blueprint, request, jsonify
from app.models.atividade_model import Atividade
from app.extensions import db_atividades
from loguru import logger

atividades = Blueprint("atividades", __name__, url_prefix="/atividades")

@atividades.route("/", methods=["POST"])
def create_atividade():
    data = request.json
    try:
        logger.info("Cadastrando atividade...")
        atividade = Atividade(
            funcional=data.get("funcional"),
            nome=data.get("nome"),
            descricao=data.get("descricao"),
            tipo=data.get("tipo"),
            duracao=data.get("duracao"),
            distancia=data.get("distancia"),
            intensidade=data.get("intensidade"),
            data=data.get("data"),
            calorias=data.get("calorias")
        )
        db_atividades.session.add(atividade)
        db_atividades.session.commit()
        logger.success("Atividade cadastrada com sucesso")
        return jsonify({"message": "Atividade criada com sucesso!", "id": atividade.id}), 201
    except Exception as e:
        db_atividades.session.rollback()
        logger.error(f"Erro ao cadastrar atividade: {e}")
        return jsonify({"error": str(e)}), 400


# Listar todas as atividades
@atividades.route("/", methods=["GET"])
def get_atividades():
    try:
        logger.info("Buscando atividades...")
        atividades_list = Atividade.query.all()
        if atividades_list:
            return jsonify([{
                "id": a.id,
                "funcional": a.funcional,
                "nome": a.nome,
                "descricao": a.descricao,
                "tipo": a.tipo,
                "duracao": a.duracao,
                "distancia": a.distancia,
                "intensidade": a.intensidade,
                "data": str(a.data),
                "calorias": a.calorias
            } for a in atividades_list])
        else:
            return jsonify({"message": "Nenhuma atividade encontrada"}), 404
    except Exception as e:
        logger.error(f"Erro ao buscar atividades: {e}")
        return jsonify({"error": str(e)}), 400

    


@atividades.route("/<string:funcional>", methods=["GET"])
def get_atividades_by_funcional(funcional):
    atividade = Atividade.query.filter_by(funcional=funcional).first()
    if atividade:
        try:
            return jsonify({
                "id": atividade.id,
                "funcional": atividade.funcional,
                "nome": atividade.nome,
                "descricao": atividade.descricao,
                "tipo": atividade.tipo,
                "duracao": atividade.duracao,
                "distancia": atividade.distancia,
                "intensidade": atividade.intensidade,
                "data": str(atividade.data),
                "calorias": atividade.calorias
            })
        except Exception as e:
            logger.error(f"Erro ao buscar atividades: {e}")
            return jsonify({"error": str(e)}), 400
    return jsonify({"message": "Atividade não encontrada"}), 404
