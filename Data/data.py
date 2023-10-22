import sqlite3

conn = sqlite3.connect('PostData.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS publicaciones (
        post_id INTEGER PRIMARY KEY,
        titulo TEXT,
        subtitulo TEXT,
        imgPost TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS secciones (
        seccion_id INTEGER PRIMARY KEY,
        post_id INTEGER,
        titulo TEXT,
        FOREIGN KEY (post_id) REFERENCES publicaciones (post_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS parrafos (
        parrafo_id INTEGER PRIMARY KEY,
        seccion_id INTEGER,
        texto TEXT,
        FOREIGN KEY (seccion_id) REFERENCES secciones (seccion_id)
    )
''')

conn.commit()
conn.close()