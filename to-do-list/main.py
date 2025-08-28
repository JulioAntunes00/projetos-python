def exibir_menu():
    print("..::MENU DE TAREFAS::..")
    print("1. Listar tarefas")
    print("2. Adicionar tarefas")
    print("3. Remover tarefas")
    print("4. Sair")
    print("::::::::::::::::::::::")

def main():
    while True:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))

if __name__ == "__main__":
    main()
