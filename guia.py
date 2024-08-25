from tkinter import *

def mostrar_guia():
    guia = Tk()
    guia.title("Guia de Boas-Vindas")

    Label(guia, text="Bem-vindo à nossa Igreja!").pack()
    Label(guia, text="Horários dos Cultos: Domingo - 10h, Quarta - 19h").pack()
    Label(guia, text="Grupos Disponíveis: Jovens, Casais, Crianças").pack()
    Label(guia, text="Missão: Servir a Deus e ao próximo com amor.").pack()

    guia.mainloop()
