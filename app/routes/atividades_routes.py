from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.services.atividade_service import AtividadeService
from app.schemas.atividade_schema import AtividadeSchema

atividades = Blueprint("atividades", __name__, url_prefix="/atividades")

atividade_schema = AtividadeSchema()
atividades_schema = AtividadeSchema(many=True)

@atividades.route("/", methods=["POST"])
def create_atividade():
    try:
        data = atividade_schema.load(request.json)
        atividade = AtividadeService.criar_atividade(data)
        return jsonify({"message": "Atividade criada!", "id": atividade.id}), 201
    except ValidationError as err:
        return jsonify({"error": str(err)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@atividades.route("/", methods=["GET"])
def get_atividades():
    try:
        atividades_list = AtividadeService.listar_atividades()
        return jsonify(atividades_schema.dump(atividades_list)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@atividades.route("/<string:funcional>", methods=["GET"])
def get_atividades_by_funcional(funcional):
    try:
        atividades_list = AtividadeService.buscar_por_funcional(funcional)
        return jsonify(atividades_schema.dump(atividades_list)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

