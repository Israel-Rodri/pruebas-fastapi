from pydantic import BaseModel, Field
from typing import Optional

#Los modelos de pydantic permiten validar los datos pasados a traves de la api
#Pydantic define que datos deben llegar del usuario, como deben venir esos datos y 
#aplica restricciones personalizadas

class Movie(BaseModel):
    id: int = Field()
    title: str = Field(min_length=1, max_length=100)
    year: int = Field(gt=1900, lt=2100)
    category: str = Field(min_length=5, max_length=50)
    duration: Optional[int] = None