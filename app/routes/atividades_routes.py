from flask import Blueprint

atividades = Blueprint("atividades", __name__, url_prefix="/atividades")


@atividades.route("/atividades", methods=["POST"])
def create_atividade():
    #TODO implementar método de criar atividade no banco de dados
    pass

@atividades.route("/atividades", methods=["GET"])
def get_atividades():
    #TODO: implementar um método que retorna todas as atividades do banco de dados
    pass

@atividades.route("/atividades/{funcional}", methods=["GET"])
def get_atividades_by_id():
    #TODO: Implementar um método que retorna a atividade pelo ID via query parameter
    pass
