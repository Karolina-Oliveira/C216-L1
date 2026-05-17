# C216 - Gerenciador de Alunos

API CRUD de alunos feita com FastAPI, Docker Compose, PostgreSQL e testes automatizados.

## Requisitos atendidos

- CRUD completo de alunos
- Endpoints em `/api/v1/alunos/`
- Geração automática de matrícula por curso
- ID no formato `CURSO + matrícula`, exemplo: `GES1`, `GEC1`
- ID não é reutilizado após remover aluno
- Execução com Docker Compose
- Persistência em PostgreSQL
- Testes automatizados de API

## Como executar a API

```bash
docker compose up --build backend
```

Swagger:

```txt
http://localhost:8000/docs
```

## Como executar os testes

```bash
docker compose run --rm tests
```

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/api/v1/alunos/` | Cadastra aluno |
| GET | `/api/v1/alunos/` | Lista alunos |
| GET | `/api/v1/alunos/{aluno_id}` | Busca aluno por ID |
| PATCH | `/api/v1/alunos/{aluno_id}` | Atualiza aluno |
| DELETE | `/api/v1/alunos/{aluno_id}` | Remove aluno |
| DELETE | `/api/v1/alunos/` | Reseta a lista |

## Exemplo de cadastro

```json
{
  "nome": "Ana",
  "email": "ana@email.com",
  "curso": "GES"
}
```
