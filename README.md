# Gerenciador de Alunos - C216

Projeto desenvolvido para a disciplina de Sistemas Distribuídos utilizando FastAPI, PostgreSQL, Docker e Flask.

## Funcionalidades

### Backend (FastAPI)

CRUD completo de alunos:

* Criar aluno
* Listar alunos
* Buscar aluno por ID
* Atualizar aluno
* Remover aluno
* Resetar lista de alunos

### Regras implementadas

* Cursos disponíveis:

  * GES
  * GEC
* Matrícula gerada automaticamente por curso
* ID sequencial por curso:

  * GES1
  * GES2
  * GEC1
  * GEC2
* IDs não são reutilizados após remoção
* Persistência utilizando PostgreSQL

### Frontend (Flask)

Páginas implementadas:

* Home
* About
* Contact

O frontend consome os dados da API FastAPI.

---

# Tecnologias Utilizadas

## Backend

* Python 3.11
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic

## Frontend

* Flask
* HTML
* CSS

## DevOps

* Docker
* Docker Compose
* Pytest

---

# Estrutura do Projeto

```txt
C216-L1/
├── pratica_5/
│   ├── app/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── tests/
│   ├── img/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── pytest.ini
│
├── pratica_6/
│   └── frontend/
│       ├── templates/
│       ├── static/
│       ├── app.py
│       └── Dockerfile
│
└── docker-compose.yml
```

---

# Como Executar

## Subir containers

```bash
docker compose up --build
```

---

# Serviços

## Backend

```txt
http://localhost:8000
```

## Swagger

```txt
http://localhost:8000/docs
```

## Frontend

```txt
http://localhost:3000
```

## Páginas do frontend

```txt
http://localhost:3000/
http://localhost:3000/about
http://localhost:3000/contact
```

---

# Executar Testes

```bash
docker compose run --rm tests
```

---

# Validar Persistência

1. Criar um aluno no Swagger
2. Parar os containers:

```bash
docker compose down
```

3. Subir novamente:

```bash
docker compose up
```

4. Verificar se os dados continuam salvos

A persistência é feita utilizando volume Docker no PostgreSQL.

---

# Endpoints

## Criar aluno

```http
POST /api/v1/alunos/
```

## Listar alunos

```http
GET /api/v1/alunos/
```

## Buscar aluno por ID

```http
GET /api/v1/alunos/{aluno_id}
```

## Atualizar aluno

```http
PATCH /api/v1/alunos/{aluno_id}
```

## Remover aluno

```http
DELETE /api/v1/alunos/{aluno_id}
```

## Resetar alunos

```http
DELETE /api/v1/alunos/
```

---

# Exemplo de JSON

## Criar aluno

```json
{
  "nome": "Ana",
  "email": "ana@email.com",
  "curso": "GES"
}
```

## Atualizar aluno

```json
{
  "nome": "Ana Maria"
}
```

---

# Testes Implementados

* Adição de 3 alunos por curso
* Listagem de alunos
* Busca por ID
* Atualização de dados
* Remoção de aluno
* Validação de persistência
* Validação de ID sequencial
* Validação de não reutilização de IDs

---

# Evidências

Os prints solicitados pela atividade estão disponíveis na pasta:

```txt
img/
```

ou

```txt
pratica_5/img/
```

---

# Autor

Karolina Oliveira

Matrícula: 115
