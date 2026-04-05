from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from models.anio_seccion import AnioSeccion

router = APIRouter(prefix="/anio-seccion", tags=["Año y Seccion"])

@router.post("/", response_model=AnioSeccion)
def create_anio_seccion(data: AnioSeccion, session: Session = Depends(get_session)):
    anio_seccion_existente = session.exec(
        select(AnioSeccion).where(
            AnioSeccion.anio == data.anio,
            AnioSeccion.seccion == data.seccion
        )
    ).first()
    if anio_seccion_existente:
        raise HTTPException(status_code=409, detail="El año y la seccion ya se encuentran registrados")
    anio_seccion_db = AnioSeccion.model_validate(data.model_dump())
    session.add(anio_seccion_db)
    session.commit()
    session.refresh(anio_seccion_db)
    return anio_seccion_db

@router.get ("/", response_model=list[AnioSeccion])
def get_all_anio_seccion(session: Session = Depends(get_session)):
    query = select(AnioSeccion)
    result = session.exec(query)
    if not result:
        raise HTTPException(status_code=404, detail="Anio y seccion no encontrados")
    return result.all()

@router.delete("/{id}")
def delete_anio_seccion(anio_seccion_id: int, session: Session = Depends(get_session)):
    anio_seccion = session.get(AnioSeccion, anio_seccion_id)
    if not anio_seccion:
        raise HTTPException(status_code=404, detail="Año y seccion no encontrados")
    session.delete(anio_seccion)
    session.commit()
    return {"message":"Año y seccion eliminados de forma exitosa"}