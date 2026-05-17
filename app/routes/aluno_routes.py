from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.aluno_schema import AlunoCreate, AlunoResponse, AlunoUpdate
from app.services import aluno_service

router = APIRouter(prefix="/api/v1/alunos", tags=["Alunos"])


@router.post("/", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def criar_aluno(payload: AlunoCreate, db: Session = Depends(get_db)):
    return aluno_service.criar_aluno(db, payload)


@router.get("/", response_model=list[AlunoResponse])
def listar_alunos(db: Session = Depends(get_db)):
    return aluno_service.listar_alunos(db)


@router.get("/{aluno_id}", response_model=AlunoResponse)
def buscar_aluno(aluno_id: str, db: Session = Depends(get_db)):
    return aluno_service.buscar_aluno_por_id(db, aluno_id)


@router.patch("/{aluno_id}", response_model=AlunoResponse)
def atualizar_aluno(aluno_id: str, payload: AlunoUpdate, db: Session = Depends(get_db)):
    return aluno_service.atualizar_aluno(db, aluno_id, payload)


@router.delete("/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_aluno(aluno_id: str, db: Session = Depends(get_db)):
    aluno_service.remover_aluno(db, aluno_id)
    return None


@router.delete("/", status_code=status.HTTP_200_OK)
def resetar_alunos(db: Session = Depends(get_db)):
    aluno_service.resetar_alunos(db)
    return {"mensagem": "Lista de alunos resetada com sucesso"}
