print("LISTA DE FRUTAS")

lista = ["Uva", "Banana", "Melancia", "Abacate"]

#def menu():
  #menu = input("Escolha uma opção:\n 1. Adicionar \n 2. Remover\n 3. Listar\n 4. Ordenar\n 0. Sair\n")
while True:
  menu = input("Escolha uma opção:\n 1. Adicionar \n 2. Remover\n 3. Listar\n 4. Ordenar\n 0. Sair\n")
  if menu == "1":
    adicionar = input("Digite a fruta para adicionar")
    lista.append(adicionar)
    print(lista)
  elif menu == "2":
    remover = input("Qual fruta deseja remover?")
    if remover in lista:
      lista.remove(remover)
      print(lista)
        
  elif menu == "3":
    print(lista)
    
  elif menu == "4":
    lista.sort()
    print("Lista ordenada:", lista)
      
  elif menu == "0":
    break
  else:
    print("Opção inválida")
    menu