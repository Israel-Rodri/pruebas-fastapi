# diagnostic.py
"""Diagnóstico completo de configuración"""

import sys

def check_dotenv():
    print("🔍 [1/5] Verificando python-dotenv...")
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("   ✅ load_dotenv() funciona")
        return True
    except ImportError:
        print("   ❌ python-dotenv no instalado: pip install python-dotenv")
        return False

def check_os_env():
    print("\n🔍 [2/5] Verificando variables de entorno...")
    import os
    url = os.getenv("DATABASE_URL")
    if url:
        print(f"   ✅ DATABASE_URL definida: {url[:40]}...")
        return True
    else:
        print("   ⚠️ DATABASE_URL no definida, verificando componentes...")
        components = {
            'POSTGRES_USER': os.getenv('POSTGRES_USER'),
            'POSTGRES_PASSWORD': '***' if os.getenv('POSTGRES_PASSWORD') else None,
            'POSTGRES_HOST': os.getenv('POSTGRES_HOST'),
            'POSTGRES_PORT': os.getenv('POSTGRES_PORT'),
            'POSTGRES_DB': os.getenv('POSTGRES_DB'),
        }
        for k, v in components.items():
            status = "✅" if v else "❌"
            print(f"   {status} {k}: {v}")
        return all(components.values())

def check_engine():
    print("\n🔍 [3/5] Verificando creación del engine...")
    try:
        from database import engine, DATABASE_URL
        print(f"   ✅ Engine creado: {type(engine).__name__}")
        print(f"   ✅ URL tipo: {type(DATABASE_URL).__name__}")
        return True
    except Exception as e:
        print(f"   ❌ Error creando engine: {e}")
        return False

def check_models():
    print("\n🔍 [4/5] Verificando import de modelos...")
    try:
        from models import (
            AnioSeccion, Estudiante, Materia,
            Nota, Profesor, ProfesorMateria
        )
        modelos = [AnioSeccion, Estudiante, Materia, Nota, Profesor, ProfesorMateria]
        for m in modelos:
            assert hasattr(m, "__tablename__")
        print(f"   ✅ {len(modelos)} modelos importados con __tablename__")
        return True
    except Exception as e:
        print(f"   ❌ Error importando modelos: {e}")
        return False

def check_connection():
    print("\n🔍 [5/5] Probando conexión real a PostgreSQL...")
    try:
        from database import engine
        from sqlmodel import text
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1;"))
            result.scalar()
        print("   ✅ Conexión a PostgreSQL exitosa")
        return True
    except Exception as e:
        print(f"   ❌ Error de conexión: {type(e).__name__}: {e}")
        return False

if __name__ == "__main__":
    print("🩺 DIAGNÓSTICO DE CONFIGURACIÓN\n" + "="*40)
    
    results = [
        check_dotenv(),
        check_os_env(), 
        check_engine(),
        check_models(),
        check_connection(),
    ]
    
    print("\n" + "="*40)
    if all(results):
        print("🎉 ¡TODO CONFIGURADO CORRECTAMENTE!")
        print("🚀 Ejecuta: python create_tables.py")
        sys.exit(0)
    else:
        print("⚠️ Se encontraron problemas. Corrige los ❌ antes de continuar.")
        sys.exit(1)