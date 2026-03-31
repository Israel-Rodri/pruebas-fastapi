from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from models.estudiante import Estudiante

router = APIRouter(prefix="/estudiante", tags=["Estudiantes"])

@router.post("/", response_model=Estudiante)
def create_estudiante(data: Estudiante, session: Session = Depends(get_session)):
    estudiante_db = Estudiante.model_validate(data.model_dump)
    session.add(estudiante_db)
    session.commit()
    session.refresh(estudiante_db)
    return estudiante_db