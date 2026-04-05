from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from typing import Optional
from models.estudiante import Estudiante
from models.anio_seccion import AnioSeccion

router = APIRouter(prefix="/estudiante", tags=["Estudiantes"])

@router.post("/", response_model=Estudiante)
def create_estudiante(data: Estudiante, session: Session = Depends(get_session)):
    estudiante_db = Estudiante.model_validate(data.model_dump())
    session.add(estudiante_db)
    session.commit()
    session.refresh(estudiante_db)
    return estudiante_db

@router.get("/", response_model=list[Estudiante])
def get_all_estudiante(anio_seccion_id: Optional[int]=None, session: Session = Depends(get_session)):
    query = select(Estudiante)
    if (anio_seccion_id):
        query = query.where(Estudiante.anio_seccion_id == anio_seccion_id)
    #incluir relacion con anio_seccion
    query = query.join(AnioSeccion, isouter=True)
    result = session.exec(query)
    if not result:
        raise HTTPException(status_code=404, detail="No se encuentran estudiantes registrados")
    return result.all()