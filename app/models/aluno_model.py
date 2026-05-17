from sqlalchemy import Column, Integer, String

from app.database.connection import Base


class AlunoModel(Base):
    __tablename__ = "alunos"

    id = Column(String, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    curso = Column(String, nullable=False, index=True)
    matricula = Column(Integer, nullable=False)


class CursoSequenceModel(Base):
    __tablename__ = "curso_sequences"

    curso = Column(String, primary_key=True, index=True)
    proxima_matricula = Column(Integer, nullable=False, default=1)
