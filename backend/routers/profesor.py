from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from models.profesor import Profesor

router = APIRouter(prefix="/profesor", tags=["Profesores"])

@router.post("/", response_model=Profesor)
def create_profesor(data: Profesor, session: Session = Depends(get_session)):
    profesor_db = Profesor.model_validate(data.model_dump())
    if Profesor.ci == data.ci:
        raise HTTPException(status_code=409, detail="El profesor ya se encuentra registrado")
    session.add(profesor_db)
    session.commit()
    session.refresh(profesor_db)
    return profesor_db

@router.get("/", response_model=list[Profesor])
def get_all_profesor(session: Session = Depends(get_session)):
    result = session.exec(select(Profesor))
    if not result:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return result.all()