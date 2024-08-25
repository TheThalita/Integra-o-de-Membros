from tkinter import *
from db import conectar

def ver_membros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM membros')
    membros = cursor.fetchall()
    conn.close()

    # Criando a interface para exibir os membros e permitir edição/exclusão
    janela = Tk()
    janela.title("Membros Cadastrados")

    if membros:
        for membro in membros:
            texto = f"ID: {membro[0]}, Nome: {membro[1]}, Telefone: {membro[2]}, Email: {membro[3]}"
            Label(janela, text=texto).pack()

            # Botão para editar membro
            Button(janela, text="Editar", command=lambda m=membro: editar_membro(m[0])).pack()

            # Botão para excluir membro
            Button(janela, text="Excluir", command=lambda m=membro: excluir_membro(m[0])).pack()
    else:
        Label(janela, text="Nenhum membro cadastrado.").pack()

    janela.mainloop()

def excluir_membro(membro_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM membros WHERE id = ?', (membro_id,))
    conn.commit()
    conn.close()
    ver_membros()  # Atualiza a lista após exclusão

def editar_membro(membro_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM membros WHERE id = ?', (membro_id,))
    membro = cursor.fetchone()
    conn.close()

    # Interface gráfica para editar membro
    janela_editar = Tk()
    janela_editar.title("Editar Membro")

    Label(janela_editar, text="Nome:").pack()
    nome = Entry(janela_editar)
    nome.insert(0, membro[1])
    nome.pack()

    Label(janela_editar, text="Telefone:").pack()
    telefone = Entry(janela_editar)
    telefone.insert(0, membro[2])
    telefone.pack()

    Label(janela_editar, text="Email:").pack()
    email = Entry(janela_editar)
    email.insert(0, membro[3])
    email.pack()

    Button(janela_editar, text="Salvar", command=lambda: salvar_edicao(membro_id, nome.get(), telefone.get(), email.get(), janela_editar)).pack()

def salvar_edicao(membro_id, nome, telefone, email, janela_editar):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE membros SET nome = ?, telefone = ?, email = ? WHERE id = ?', (nome, telefone, email, membro_id))
    conn.commit()
    conn.close()
    janela_editar.destroy()  # Fecha a janela de edição
    ver_membros()  # Atualiza a lista após a edição
