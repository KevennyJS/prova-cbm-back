from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_add_usuario_valido():
    response = client.post(
        "/perfis",
        json={
            "tipos_sanguineo_id": 1,
            "signo_id": 1,
            "cpf": "54746622205",
            "nome": "Kevenny de Jesus Santos",
            "data_nascimento": "2000-06-23T00:00:01.001Z",
            "email": "kevennykeke@gmail.com",
            "telefone": "79998836127",
            "resumo": "olá, meu nome é kevenny"
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Perfil cadastrado com sucesso"}


def test_add_usuario_menor_idade():
    response = client.post(
        "/perfis",
        json={
            "tipos_sanguineo_id": 1,
            "signo_id": 1,
            "cpf": "54746622205",
            "nome": "Kevenny de Jesus Santos",
            "data_nascimento": "2010-06-23T00:00:01.001Z",
            "email": "kevennykeke@gmail.com",
            "telefone": "7998836127",
            "resumo": "olá, meu nome é kevenny"
        },
    )
    assert response.status_code == 404
    assert response.json() == {"message": "O perfil deve ter mais de 18 anos"}



