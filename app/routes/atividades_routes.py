from flask import Blueprint, request, jsonify
from app.services.atividade_service import AtividadeService

atividades = Blueprint("atividades", __name__, url_prefix="/atividades")

@atividades.route("/", methods=["POST"])
def create_atividade():
    try:
        data = request.json
        atividade = AtividadeService.criar_atividade(data)
        return jsonify({"message": "Atividade criada!", "id": atividade.id}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

@atividades.route("/", methods=["GET"])
def get_atividades():
    try:
        atividades_list = AtividadeService.listar_atividades()
        return jsonify([a.to_dict() for a in atividades_list])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@atividades.route("/<string:funcional>", methods=["GET"])
def get_atividades_by_funcional(funcional):
    try:
        atividades_list = AtividadeService.buscar_por_funcional(funcional)
        return jsonify([a.to_dict() for a in atividades_list])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@atividades.route("/<int:id>", methods=["PUT"])
def edit_atividade_by_id(id):
    try:
        data = request.json
        atividade = AtividadeService.editar_atividade(id, data)
        if not atividade:
            return jsonify({"error": "Atividade não encontrada"}), 404
        return jsonify({"message": "Atividade editada!", "atividade": atividade.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Deletar atividade pelo ID
@atividades.route("/<int:id>", methods=["DELETE"])
def delete_atividade_by_id(id):
    try:
        deleted = AtividadeService.deletar_atividade(id)
        if not deleted:
            return jsonify({"error": "Atividade não encontrada"}), 404
        return jsonify({"message": f"Atividade {id} deletada com sucesso!"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

