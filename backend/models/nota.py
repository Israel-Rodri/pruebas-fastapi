from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Nota(SQLModel, table=True):
    __tablename__ = "nota"

    id: Optional[int] = Field(primary_key=True)
    nota_1: int = Field(nullable=False, ge=0, le=20)
    nota_2: int = Field(nullable=False, ge=0, le=20)
    nota_3: int = Field(nullable=False, ge=0, le=20)
    estudiante_ci: int = Field(foreign_key="estudiante.ci", nullable=False)
    materia_id: int = Field(foreign_key="materia.id", nullable=False)

    estudiante: Optional["Estudiante"] = Relationship(back_populates="notas")
    materia: Optional["Materia"] = Relationship(back_populates="notas")

    @property
    def nota_final(self) -> int:
        return self.nota_1+self.nota_2+self.nota_3 / 3

    def __repr__(self) -> str:
        return f"<Nota id:{self.id} nota final:{self.nota_final}>"
