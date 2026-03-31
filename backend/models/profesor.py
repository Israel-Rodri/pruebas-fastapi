from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .materia import Materia

class Profesor(SQLModel, table=True):
    __tablename__ = "profesor"

    ci: int = Field(primary_key=True)
    primer_nom: str = Field(max_length=50, nullable=False)
    segundo_nom: Optional[str] = Field(max_length=50)
    primer_ape: str = Field(max_length=50, nullable=False)
    segundo_ape: str = Field(max_length=50, nullable=False)

    @property
    def nombre_completo(self) -> str:
        nombres = [n for n in [self.primer_nom, self.segundo_nom] if n]
        apellidos = [a for a in [self.primer_ape, self.segundo_ape] if a]
        return f"{' '.join(nombres)} {' '.join(apellidos)}"

    def __str__(self) -> str:
        return f"<Profesor CI:{self.ci} {self.nombre_completo}"