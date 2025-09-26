import pytest
from app.services.atividade_service import AtividadeService

valid_payload = {
    "funcional": "12345",
    "nome": "Corrida",
    "descricao": "Corrida 5km",
    "tipo": "Corrida",
    "duracao": 30,
    "distancia": 5.0,
    "intensidade": "Alta",
    "data": "25-09-2025",
    "calorias": 400
}

def test_criar_atividade_extra_field():
    payload = valid_payload.copy()
    payload["extra"] = "não permitido"
    with pytest.raises(ValueError) as excinfo:
        AtividadeService.criar_atividade(payload)
    assert "Campos não permitidos" in str(excinfo.value)

def test_criar_atividade_missing_field():
    payload = valid_payload.copy()
    payload.pop("nome")
    with pytest.raises(ValueError) as excinfo:
        AtividadeService.criar_atividade(payload)
    assert "Campos obrigatórios faltando" in str(excinfo.value)

def test_criar_atividade_tipo_invalido():
    payload = valid_payload.copy()
    payload["duracao"] = "30 minutos"
    with pytest.raises(ValueError) as excinfo:
        AtividadeService.criar_atividade(payload)
    assert "Campo 'duracao' inválido" in str(excinfo.value)
