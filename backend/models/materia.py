from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Materia(SQLModel, table=True):
    __tablename__ = "materia"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False, unique=True)

    notas: List["Nota"] = Relationship(
        back_populates="materia",
        sa_relationship_kwargs={"cascade":"all, delete-orphan"}
    )

    def __repr__(self) -> str:
        return f"<Materia:{self.nombre}>"
