print("\n..:LISTA DE FRUTAS!!!:..")

lista = ["Uva", "Banana", "Melancia", "Abacate"]

def menu():
  print("""
1. Adicionar
2. Remover
3. Listar
4. Ordenar
0. Sair
""")


while True:
    menu()
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        adicionar = input("Digite a fruta para adicionar: ").capitalize()
        lista.append(adicionar)
        print(lista)

    elif opcao == "2":
        remover = input("Qual fruta deseja remover?").capitalize()
        if remover in lista:
            lista.remove(remover)
            print(lista)
        
    elif opcao == "3":
        print(lista)
    
    elif opcao == "4":
        lista.sort()
        print("Lista ordenada:", lista)
      
    elif opcao == "0":
        break
    else:
        print("Opção inválida")
