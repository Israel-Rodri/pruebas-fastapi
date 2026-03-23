from database import init_db
from models.movies import Movie

if __name__ == "__main__":
    print("Creando tablas...")
    init_db()
    print("Tablas creadas de forma exitosa")