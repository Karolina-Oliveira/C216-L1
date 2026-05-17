from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.aluno_model import AlunoModel, CursoSequenceModel
from app.schemas.aluno_schema import AlunoCreate, AlunoUpdate


def _normalizar_curso(curso) -> str:
    return curso.value if hasattr(curso, "value") else str(curso).upper()


def _gerar_identificacao(db: Session, curso: str) -> tuple[str, int]:
    sequencia = db.get(CursoSequenceModel, curso)

    if sequencia is None:
        sequencia = CursoSequenceModel(curso=curso, proxima_matricula=1)
        db.add(sequencia)
        db.flush()

    matricula = sequencia.proxima_matricula
    aluno_id = f"{curso}{matricula}"
    sequencia.proxima_matricula += 1

    return aluno_id, matricula


def criar_aluno(db: Session, payload: AlunoCreate) -> AlunoModel:
    curso = _normalizar_curso(payload.curso)
    aluno_id, matricula = _gerar_identificacao(db, curso)

    aluno = AlunoModel(
        id=aluno_id,
        nome=payload.nome,
        email=str(payload.email),
        curso=curso,
        matricula=matricula,
    )

    db.add(aluno)
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não foi possível cadastrar o aluno. Verifique se o e-mail já existe.",
        )

    db.refresh(aluno)
    return aluno


def listar_alunos(db: Session) -> list[AlunoModel]:
    return db.query(AlunoModel).order_by(AlunoModel.curso, AlunoModel.matricula).all()


def buscar_aluno_por_id(db: Session, aluno_id: str) -> AlunoModel:
    aluno = db.get(AlunoModel, aluno_id.upper())

    if aluno is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")

    return aluno


def atualizar_aluno(db: Session, aluno_id: str, payload: AlunoUpdate) -> AlunoModel:
    aluno = buscar_aluno_por_id(db, aluno_id)
    dados = payload.model_dump(exclude_unset=True)

    if "nome" in dados:
        aluno.nome = dados["nome"]

    if "email" in dados:
        aluno.email = str(dados["email"])

    if "curso" in dados:
        novo_curso = _normalizar_curso(dados["curso"])
        if novo_curso != aluno.curso:
            novo_id, nova_matricula = _gerar_identificacao(db, novo_curso)
            aluno.id = novo_id
            aluno.curso = novo_curso
            aluno.matricula = nova_matricula

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não foi possível atualizar o aluno. Verifique se o e-mail já existe.",
        )

    db.refresh(aluno)
    return aluno


def remover_aluno(db: Session, aluno_id: str) -> None:
    aluno = buscar_aluno_por_id(db, aluno_id)
    db.delete(aluno)
    db.commit()


def resetar_alunos(db: Session) -> None:
    db.query(AlunoModel).delete()
    db.query(CursoSequenceModel).delete()
    db.commit()
