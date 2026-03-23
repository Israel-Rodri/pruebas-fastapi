from fastapi import FastAPI, HTTPException
from routers import movies

app = FastAPI()

app.include_router(movies.router)

@app.get("/")
def root():
    return {"message":"Pagina de inicio"}