from tkinter import *
from db import conectar

def salvar_membro(nome, telefone, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO membros (nome, telefone, email) VALUES (?, ?, ?)', (nome, telefone, email))
    conn.commit()
    conn.close()

def janela_cadastro():
    janela = Tk()
    janela.title("Cadastro de Novo Membro")

    Label(janela, text="Nome:").pack()
    nome = Entry(janela)
    nome.pack()

    Label(janela, text="Telefone:").pack()
    telefone = Entry(janela)
    telefone.pack()

    Label(janela, text="Email:").pack()
    email = Entry(janela)
    email.pack()

    Button(janela, text="Salvar", command=lambda: salvar_membro(nome.get(), telefone.get(), email.get())).pack()

    janela.mainloop()
