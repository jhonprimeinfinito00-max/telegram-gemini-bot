import sqlite3
from config import DATABASE_NAME

def iniciar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        mensaje TEXT
    )
    """)

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    iniciar_db()
