from __future__ import annotations
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class ProfesorMateria(SQLModel, table=True):
    #Tabla transicional para manejar la relacion de n-n entre profesores y materias
    #No define Relationship para evitar ciclos

    __tablename__ = "profesor_materia"

    id: Optional[int] = Field(default=None, primary_key=True)
    profesor_ci: int = Field(foreign_key="profesor.ci", nullable=False)
    materia_id: int = Field(foreign_key="materia.id", nullable=False)

    def __repr__(self) -> str:
        return f"<ProfesorMateria prof_ci:{self.profesor_ci} mat_id:{self.materia_id}"