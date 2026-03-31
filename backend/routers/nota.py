from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from models.nota import Nota

router = APIRouter(prefix="/nota", tags=["Notas"])

@router.post("/", response_model=Nota)
def create_nota(data: Nota, session: Session = Depends(get_session)):
    nota_db = Nota.model_validate(data.model_dump())
    session.add(nota_db)
    session.commit()
    session.refresh(nota_db)
    return  nota_db

@router.get("/", response_model=list[Nota])
def get_all_nota(session: Session = Depends(get_session)):
    query = select(Nota)
    result = session.exec(query)
    if not result:
        raise HTTPException(status_code=404, detail="No se han encontrado notas")
    return result.all()