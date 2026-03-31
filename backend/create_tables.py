#!/usr/bin/env python3
# create_tables.py
"""
Script para crear las tablas en PostgreSQL usando SQLModel.
Ejecutar: python create_tables.py
"""

import sys
from sqlmodel import SQLModel, text
from database import engine, DATABASE_URL

def main():
    print("🔄 Conectando a la base de datos...")
    print(f"📍 URL: {DATABASE_URL[:50]}...")  # Mostrar solo inicio por seguridad
    
    # 🔑 VALIDACIÓN CRÍTICA: Importar modelos ANTES de create_all()
    # Sin esto, SQLModel no registra las tablas en el metadata
    try:
        from models import (
            AnioSeccion, Estudiante, Materia,
            Nota, Profesor, ProfesorMateria
        )
        print("✅ Modelos importados correctamente")
    except ImportError as e:
        print(f"❌ Error importando modelos: {e}")
        print("💡 Verifica que la carpeta 'models/' tenga __init__.py")
        return 1
    
    try:
        # Crear todas las tablas
        print("🔨 Ejecutando SQLModel.metadata.create_all()...")
        SQLModel.metadata.create_all(engine)
        print("✅ Tablas creadas exitosamente!")
        
        # 📋 Listar tablas usando consulta SQL directa (compatible con SQLAlchemy 2.x)
        print("\n📋 Verificando tablas en la BD...")
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_type = 'BASE TABLE'
                    ORDER BY table_name;
                """)
            )
            tablas = [row[0] for row in result.all()]
            
            if tablas:
                print(f"✅ Tablas encontradas ({len(tablas)}):")
                for t in tablas:
                    print(f"   • {t}")
            else:
                print("⚠️ No se encontraron tablas en el esquema 'public'")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {e}")
        
        # Diagnóstico adicional
        print("\n🔍 Diagnóstico:")
        print(f"   • DATABASE_URL está definido: {bool(DATABASE_URL)}")
        print(f"   • DATABASE_URL comienza con 'postgresql+': {DATABASE_URL.startswith('postgresql+') if DATABASE_URL else False}")
        
        print("\n💡 Soluciones comunes:")
        print("   1. PostgreSQL no está corriendo → sudo systemctl start postgresql")
        print("   2. Credenciales incorrectas → Revisa .env")
        print("   3. Base de datos no existe → Crea con: createdb ejemplo_colegio")
        print("   4. psycopg2 no instalado → pip install psycopg2-binary")
        print("   5. Models no importados → Asegura que __init__.py los exporte")
        
        return 1

if __name__ == "__main__":
    sys.exit(main())