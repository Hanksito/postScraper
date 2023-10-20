import sqlite3


conn = sqlite3.connect('mi_base_de_datos.db')


cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')


conn.commit()
conn.close()
