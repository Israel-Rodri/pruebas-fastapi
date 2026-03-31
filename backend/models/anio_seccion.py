from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .estudiante import Estudiante

class AnioSeccion(SQLModel, table=True):
    __tablename__ = "anio_seccion"

    id: Optional[int] = Field(default=None, primary_key=True)
    anio: str = Field(max_length=1, nullable=False)
    seccion: str = Field(max_length=1, nullable=False)

    estudiantes: List["Estudiante"] = Relationship(
        back_populates="anio_seccion"
    )

    def __repr__(self) -> str:
        return f"<AnioSeccion {self.anio}{self.seccion}>"