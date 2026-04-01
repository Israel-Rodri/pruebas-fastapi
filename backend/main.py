from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Estudiante, Materia, Nota, Profesor, ProfesorMateria, AnioSeccion
from routers import anio_seccion, estudiante, materia, nota, profesor, profesor_materia

app = FastAPI(
    title="Sistema de Gestión de Notas",
    description="API para la gestión de notas parciales y finales de los estudiantes de educación media y diversificada de la UE Colegio Fundación Taller Escuela",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5175",
        "http://127.0.0.1:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(anio_seccion.router)
app.include_router(estudiante.router)
app.include_router(materia.router)
app.include_router(nota.router)
app.include_router(profesor.router)
app.include_router(profesor_materia.router)

@app.on_event("startup")
def on_startup():
    with engine.connect() as conn:
        print("Conexion a la BD establecida")

@app.get("/")
def root():
    return{"message":"API Colegio - Funcionando correctamente"}