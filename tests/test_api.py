from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
BASE_URL = "/api/v1/alunos/"


def setup_function():
    client.delete(BASE_URL)


def criar_aluno(nome: str, email: str, curso: str):
    return client.post(BASE_URL, json={"nome": nome, "email": email, "curso": curso})


def test_adicionar_tres_alunos_por_curso_e_listar():
    alunos = [
        ("Ana", "ana@email.com", "GES"),
        ("Bruno", "bruno@email.com", "GES"),
        ("Carla", "carla@email.com", "GES"),
        ("Diego", "diego@email.com", "GEC"),
        ("Elisa", "elisa@email.com", "GEC"),
        ("Fabio", "fabio@email.com", "GEC"),
    ]

    for nome, email, curso in alunos:
        response = criar_aluno(nome, email, curso)
        assert response.status_code == 201

    response = client.get(BASE_URL)
    assert response.status_code == 200

    body = response.json()
    assert len(body) == 6
    assert [aluno["id"] for aluno in body] == ["GEC1", "GEC2", "GEC3", "GES1", "GES2", "GES3"]


def test_buscar_aluno_por_id():
    criar_aluno("Ana", "ana@email.com", "GES")

    response = client.get(f"{BASE_URL}GES1")

    assert response.status_code == 200
    assert response.json()["id"] == "GES1"
    assert response.json()["nome"] == "Ana"


def test_atualizar_dados_do_aluno():
    criar_aluno("Ana", "ana@email.com", "GES")

    response = client.patch(f"{BASE_URL}GES1", json={"nome": "Ana Maria", "email": "ana.maria@email.com"})

    assert response.status_code == 200
    assert response.json()["nome"] == "Ana Maria"
    assert response.json()["email"] == "ana.maria@email.com"
    assert response.json()["id"] == "GES1"


def test_remover_aluno():
    criar_aluno("Ana", "ana@email.com", "GES")

    response = client.delete(f"{BASE_URL}GES1")
    assert response.status_code == 204

    response = client.get(f"{BASE_URL}GES1")
    assert response.status_code == 404


def test_id_nao_e_reutilizado_apos_delete():
    criar_aluno("Ana", "ana@email.com", "GES")
    client.delete(f"{BASE_URL}GES1")

    response = criar_aluno("Bruno", "bruno@email.com", "GES")

    assert response.status_code == 201
    assert response.json()["id"] == "GES2"
    assert response.json()["matricula"] == 2


def test_validar_persistencia_dos_dados_no_postgresql():
    criar_aluno("Ana", "ana@email.com", "GES")

    primeira_consulta = client.get(f"{BASE_URL}GES1")
    segunda_consulta = client.get(f"{BASE_URL}GES1")

    assert primeira_consulta.status_code == 200
    assert segunda_consulta.status_code == 200
    assert primeira_consulta.json() == segunda_consulta.json()
