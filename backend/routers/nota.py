from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from models.nota import Nota
from models.estudiante import Estudiante
from models.materia import Materia

router = APIRouter(prefix="/nota", tags=["Notas"])

@router.post("/", response_model=Nota)
def create_nota(data: Nota, session: Session = Depends(get_session)):
    estudiante = session.get(Estudiante, data.estudiante_ci)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    materia = session.get(Materia, data.materia_id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    nota_existente = session.exec(
        select(Nota).where(
            Nota.estudiante_ci == data.estudiante_ci,
            Nota.materia_id == data.materia_id
        )
    ).first()
    if nota_existente:
        raise HTTPException(status_code=409, detail="Ya existe una nota para este estudiante en esta materia")
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

@router.get("/estudiante/{estudiante_ci}/", response_model=list[Nota])
def get_nota_by_ci(estudiante_ci: int, session: Session = Depends(get_session)):
    estudiante = session.get(Estudiante, estudiante_ci)
    if not estudiante:
        raise HTTPException(status_code=404, detail="El estudiante no existe")
    result = session.exec(
        select(Nota).where(
            Nota.estudiante_ci == estudiante_ci
        )
    ).all()
    return result

@router.get("/materia/{materia_id}/", response_model=list[Nota])
def get_nota_by_ci(materia_id: int, session: Session = Depends(get_session)):
    materia = session.get(Materia, materia_id)
    if not materia:
        raise HTTPException(status_code=404, detail="La materia no existe")
    result = session.exec(
        select(Nota).where(
            Nota.materia_id == materia_id
        )
    ).all()
    return result