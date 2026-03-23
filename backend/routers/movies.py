from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database import get_session
from models.movies import Movie

router = APIRouter(prefix="/movies", tags=["Peliculas"])

@router.post("/", response_model=Movie)
def create_movie(movie: Movie, session: Session = Depends(get_session)):
    movie_db = Movie.model_validate(movie.model_dump())
    session.add(movie_db)
    session.commit()
    session.refresh(movie_db)
    return movie_db

@router.get("/", response_model=list[Movie])
def get_movies(session: Session = Depends(get_session)):
    query = select(Movie)
    result = session.exec(query)
    if result:
        return result
    raise HTTPException(status_code=404, detail="La tabla esta vacia")