from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Estudiante(SQLModel, table=True):
    __tablename__ = "estudiante"

    ci: int = Field(primary_key=True)
    primer_nom: str = Field(max_length=50, nullable=False)
    segundo_nom: Optional[str] = Field(max_length=50)
    primer_ape: str = Field(max_length=50, nullable=False)
    segundo_ape: str = Field(max_length=50, nullable=False)
    anio_seccion_id: Optional[int] = Field(
        default=None,
        foreign_key="anio_seccion.id",
        nullable=False
    )

    anio_seccion: Optional["AnioSeccion"] = Relationship(
        back_populates="estudiantes"
    )
    notas: List["Nota"] = Relationship(
        back_populates="estudiante",
        sa_relationship_kwargs={"cascade":"all, delete-orphan"}
    )

    @property
    def nombre_completo(self) -> str:
        nombres = [n for n in [self.primer_nom, self.segundo_nom] if n]
        apellidos = [a for a in [self.primer_ape, self.segundo_ape] if a]
        return f"{' '.join(nombres)} {' '.join(apellidos)}"

    def __repr__(self) -> str:
        return f"<Estudiante CI:{self.ci} {self.nombre_completo}"
