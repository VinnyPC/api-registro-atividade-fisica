from flask import Flask
from app.routes.atividades_routes import atividades
from app.models.atividade_model import Atividade
from flask_sqlalchemy import SQLAlchemy
import os
from loguru import logger
from dotenv import load_dotenv

db_atividades = SQLAlchemy()

load_dotenv()

def create_app():
    try:
        app = Flask(__name__)

        logger.info("Configurando banco de dados...")
        DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
        DB_PORT = int(os.getenv('DB_PORT', 3306))
        DB_USER = os.getenv('DB_USER', 'root')
        DB_PASS = os.getenv('DB_PASS', '')
        DB_NAME = os.getenv('DB_NAME', 'db_atividades')

        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db_atividades.init_app(app)

        logger.info("Registrando blueprints")
        app.register_blueprint(atividades)

        return app
    except Exception as e:
        logger.error(f"Erro ao configurar banco de dados: {e}")
        raise
