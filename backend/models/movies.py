from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import Optional

class Movie(SQLModel, table=True):
    movie_id: int | None = Field(default=None, primary_key=True)
    movie_title: str = Field(min_length=2, max_length=100)
    movie_year: int = Field(gt=1900, lt=2050)
    movie_genre: str = Field(min_length=1, max_length=50)