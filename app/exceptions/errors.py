from flask import Flask, jsonify
from marshmallow import ValidationError
import traceback

def register_error_handlers(app: Flask):
    # Erros de validação do Marshmallow
    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({
            "error": "Erro de validação",
            "messages": err.messages  # mostra quais campos falharam
        }), 400

    # Erros de banco de dados (SQLAlchemy, por ex.)
    @app.errorhandler(Exception)
    def handle_generic_error(err):
        # Aqui você decide se mostra o traceback ou não
        return jsonify({
            "error": "Erro interno no servidor",
            "details": str(err),
            # "trace": traceback.format_exc()  # cuidado em prod
        }), 500
