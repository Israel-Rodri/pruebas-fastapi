from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True, #Para ver sonsultas sql en consola
    pool_pre_ping=True, #verifica conexiones antes de usarlas
    pool_size=5, #Conexiones maximas en pool
    max_overflow=10 #Conexiones extra temporales
)

def get_session():
    #Crea sesion por cada request
    with Session(engine) as session:
        yield session

def init_db():
    #Crea las tablas si no existen
    from models import (
        AnioSeccion, Estudiante, Materia, Nota, Profesor, ProfesorMateria
    )
    SQLModel.metadata.create_all(engine)

#Exporta engine para usarlo en create_tables
__all__ = ["engine", "get_session", "init_db", "DATABASE_URL"]