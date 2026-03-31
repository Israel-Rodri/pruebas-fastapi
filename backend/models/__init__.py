from __future__ import annotations
from .anio_seccion import AnioSeccion
from .profesor import Profesor
from .materia import Materia
from .profesor_materia import ProfesorMateria
from .estudiante import Estudiante
from .nota import Nota

for modelo in [AnioSeccion, Estudiante, Materia, Nota, Profesor]:
    try:
        modelo.model_rebuild()
    except Exception:
        pass

__all__ = [
    "AnioSeccion",
    "Estudiante",
    "Materia",
    "Nota",
    "Profesor",
    "ProfesorMateria"
]