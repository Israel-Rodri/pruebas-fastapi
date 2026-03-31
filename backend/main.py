from fastapi import FastAPI, HTTPException, Depends, status
from sqlmodel import Session, select
from typing import List

from database import get_session, engine
from models import Estudiante, Materia, Nota, Profesor, ProfesorMateria, AnioSeccion
from routers import anio_seccion, estudiante

app = FastAPI(
    title="Sistema de Gestión de Notas",
    description="API para la gestión de notas parciales y finales de los estudiantes de educación media y diversificada de la UE Colegio Fundación Taller Escuela",
    version="1.0.0"
)

app.include_router(anio_seccion.router)
app.include_router(estudiante.router)

@app.on_event("startup")
def on_startup():
    with engine.connect() as conn:
        print("Conexion a la BD establecida")

@app.get("/")
def root():
    return{"message":"API Colegio - Funcionando correctamente"}