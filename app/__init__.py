from flask import Flask
from .routes.atividades import atividades

def create_app():
    app = Flask(__name__)

    #TODO: registrar outros blueprints posteriormente para novas rotas, manter tudo separado e organizado por arquivos
    app.register_blueprint(atividades)

    return app