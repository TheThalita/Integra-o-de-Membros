import sqlite3

def criar_bd():
    conn = sqlite3.connect('igreja.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS membros (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY,
            membro_id INTEGER,
            comentario TEXT,
            data TEXT,
            FOREIGN KEY(membro_id) REFERENCES membros(id)
        )
    ''')
    conn.commit()
    conn.close()

def conectar():
    return sqlite3.connect('igreja.db')
