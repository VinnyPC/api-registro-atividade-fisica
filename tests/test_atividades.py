import json

def test_create_atividade(client):
    payload = {
        "funcional": "001",
        "dataHora": "2025-01-15T10:00:00",
        "codigoAtividade": "BASKET",
        "descricaoAtividade": "Treino de basquete"
    }

    response = client.post("/atividades/", json=payload)
    data = response.get_json()

    assert response.status_code == 201
    assert "id" in data
    assert data["message"] == "Atividade criada!"


def test_create_atividade_invalid(client):
    payload = {"codigoAtividade": "RUN"}  # falta campos obrigatórios como funcional e dataHora

    response = client.post("/atividades/", json=payload)
    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data


def test_get_atividades(client):
    payload1 = {
        "funcional": "001",
        "dataHora": "2025-01-15T10:00:00",
        "codigoAtividade": "BASKET",
        "descricaoAtividade": "Basquete 3x3"
    }
    payload2 = {
        "funcional": "002",
        "dataHora": "2025-01-16T07:00:00",
        "codigoAtividade": "RUN",
        "descricaoAtividade": "Corrida 5km"
    }
    client.post("/atividades/", json=payload1)
    client.post("/atividades/", json=payload2)

    response = client.get("/atividades/")
    data = response.get_json()
    assert response.status_code == 200
    assert data["total"] >= 2
    assert isinstance(data["itens"], list)
    assert len(data["itens"]) >= 2

    response = client.get("/atividades/?codigoAtividade=RUN")
    data = response.get_json()
    assert response.status_code == 200
    assert all(item["codigoAtividade"] == "RUN" for item in data["itens"])
    assert data["total"] == len(data["itens"])



