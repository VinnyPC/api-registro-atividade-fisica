import pytest
from app import create_app
from app.extensions import db_atividades
from app.models.atividade_model import Atividade

@pytest.fixture
def client():
    app = create_app() 
    app.config["TESTING"] = True
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db_atividades.create_all()
        yield app.test_client()
        db_atividades.session.remove()
        db_atividades.drop_all()


def test_create_atividade(client):
    payload = {
        "funcional": "000000",
        "nome": "testestes",
        "descricao": "test",
        "tipo": "test",
        "duracao": 120,
        "distancia": 50,
        "intensidade": "test",
        "data": "2025-09-25",
        "calorias": 1500
    }
    response = client.post("/atividades/", json=payload)
    data = response.get_json()

    assert response.status_code == 201
    assert "id" in data
    assert data["message"] == "Atividade criada com sucesso!"


def test_get_atividades_empty(client):
    response = client.get("/atividades/")
    data = response.get_json()

    assert response.status_code == 404
    assert data["message"] == "Nenhuma atividade encontrada"


def test_get_atividades(client):
    atividade = Atividade(
        funcional="000000",
        nome="testestes",
        descricao="test",
        tipo="test",
        duracao=120,
        distancia=50,
        intensidade="test",
        data="2025-09-25",
        calorias=1500
    )
    db_atividades.session.add(atividade)
    db_atividades.session.commit()

    response = client.get("/atividades/")
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert data[0]["nome"] == "testestes"


def test_get_atividades_by_funcional(client):
    atividade = Atividade(
        funcional="000000",
        nome="Teste nome",
        descricao="Teste desc",
        tipo="test",
        duracao=120,
        distancia=50,
        intensidade="test",
        data="2025-09-25",
        calorias=1500
    )
    db_atividades.session.add(atividade)
    db_atividades.session.commit()

    response = client.get("/atividades/000000")
    data = response.get_json()

    assert response.status_code == 200
    assert data["nome"] == "Teste nome"


def test_get_atividades_by_funcional_not_found(client):
    response = client.get("/atividades/vinivini")
    data = response.get_json()

    assert response.status_code == 404
    assert data["message"] == "Atividade não encontrada"
