from tkinter import *
from db import conectar

def salvar_feedback(membro_id, comentario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (membro_id, comentario, data) VALUES (?, ?, date("now"))', (membro_id, comentario))
    conn.commit()
    conn.close()

def janela_feedback():
    janela = Tk()
    janela.title("Feedback dos Membros")

    Label(janela, text="ID do Membro:").pack()
    membro_id = Entry(janela)
    membro_id.pack()

    Label(janela, text="Comentário:").pack()
    comentario = Entry(janela)
    comentario.pack()

    Button(janela, text="Enviar", command=lambda: salvar_feedback(membro_id.get(), comentario.get())).pack()

    janela.mainloop()
