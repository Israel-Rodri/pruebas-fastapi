from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from models.profesor_materia import ProfesorMateria
from models.profesor import Profesor
from models.materia import Materia

router = APIRouter(prefix="/profesor-materia", tags=["Relacion entre Profesores y Materias"])

@router.post("/", response_model=ProfesorMateria)
def relate_profesor_materia(data: ProfesorMateria, session: Session = Depends(get_session)):
    profesor = session.get(Profesor, data.profesor_ci)
    if not profesor:
        raise HTTPException(status_code=404, detail="El profesor no existe")
    materia = session.get(Materia, data.materia_id)
    if not materia:
        raise HTTPException(status_code=404, detail="La materia no existe")
    relacion_existente = session.exec(
        select(ProfesorMateria).where(
            ProfesorMateria.profesor_ci == data.profesor_ci,
            ProfesorMateria.materia_id == data.materia_id
        )
    )
    if relacion_existente:
        raise HTTPException(status_code=409, detail="La relacion entre profesor y materia ya existe")
    profesor_materia_db = ProfesorMateria.model_validate(data.model_dump())
    session.add(profesor_materia_db)
    session.commit()
    session.refresh(profesor_materia_db)
    return profesor_materia_db