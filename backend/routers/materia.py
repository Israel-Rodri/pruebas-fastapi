from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from models.materia import Materia

router = APIRouter(prefix="/materia", tags=["Materias"])

@router.post("/", response_model=Materia)
def create_materia(data: Materia, session: Session = Depends(get_session)):
    materia_db = Materia.model_validate(data.model_dump())
    session.add(materia_db)
    session.commit()
    session.refresh(materia_db)
    return materia_db

@router.get("/", response_model=list[Materia])
def get_all_materia(session: Session = Depends(get_session)):
    query = select(Materia)
    result = session.exec(query)
    if not result:
        raise HTTPException(status_code=404, detail="No se han encontrado materias")
    return result.all()