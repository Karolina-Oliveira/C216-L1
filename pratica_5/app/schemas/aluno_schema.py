from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class Curso(str, Enum):
    GES = "GES"
    GEC = "GEC"


class AlunoCreate(BaseModel):
    nome: str = Field(..., min_length=1)
    email: EmailStr
    curso: Curso


class AlunoUpdate(BaseModel):
    nome: Optional[str] = Field(default=None, min_length=1)
    email: Optional[EmailStr] = None
    curso: Optional[Curso] = None


class AlunoResponse(BaseModel):
    id: str
    nome: str
    email: EmailStr
    curso: Curso
    matricula: int

    class Config:
        from_attributes = True
