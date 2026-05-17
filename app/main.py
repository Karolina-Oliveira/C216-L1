from fastapi import FastAPI

from app.database.connection import Base, engine
from app.routes.aluno_routes import router as aluno_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gerenciador de Alunos",
    description="API CRUD de alunos com FastAPI, Docker e PostgreSQL",
    version="1.0.0",
)

app.include_router(aluno_router)


@app.get("/")
def root():
    return {"status": "API funcionando"}
