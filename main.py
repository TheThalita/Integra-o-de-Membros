from cadastro import janela_cadastro
from guia import mostrar_guia
from feedback import janela_feedback
from verificar_membros import ver_membros
from db import criar_bd

def main():
    criar_bd()

    while True:
        print("\nSistema de Integração de Novos Membros")
        print("1. Cadastro de Novo Membro")
        print("2. Guia de Boas-Vindas")
        print("3. Enviar Feedback")
        print("4. Verificar, Editar ou Excluir Membros Cadastrados")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            janela_cadastro()
        elif escolha == '2':
            mostrar_guia()
        elif escolha == '3':
            janela_feedback()
        elif escolha == '4':
            ver_membros()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
