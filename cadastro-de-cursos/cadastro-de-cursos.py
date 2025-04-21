import os

# Função para limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função para criar linhas para o melhor visual
def linha(tamanho=45):
    print("=" * tamanho)


# Função para exibir o menu principal
def menu_principal():
    while True:
        limpar_tela()
        linha()
        print("   🎓 BEM-VINDO AO SISTEMA LMS TERMINAL 🎓   ")
        linha()
        print("1️⃣ Criar Novo Usuário")
        print("2️⃣ Fazer Login")
        print("3️⃣ Sair\n")
        escolha = input("🔹 Escolha uma opção: ")

        if escolha == "1":
            criar_usuario()
        elif escolha == "2":
            if fazer_login():
                painel_principal()
        elif escolha == "3":
            print("\n👋 Saindo do sistema... Até mais!\n")
            break
        else:
            input("\n❌ Opção inválida! Pressione ENTER para tentar novamente...")

# Função para criar usuário
def criar_usuario():
    limpar_tela()
    linha()
    print("          🆕 CRIAÇÃO DE USUÁRIO         ")
    linha()
    nome = input("👤 Nome: ")
    email = input("📧 E-mail: ")
    senha = input("🔒 Crie uma senha: ")
    print("\n✅ Usuário criado com sucesso!\n")
    input("🔹 Pressione ENTER para continuar...")

# Função para fazer login
def fazer_login():
    limpar_tela()
    linha()
    print("               🔑 LOGIN                ")
    linha()
    email = input("📧 E-mail: ")
    senha = input("🔒 Senha: ")
    print("\n✅ Login realizado com sucesso!\n")
    input("🔹 Pressione ENTER para acessar o painel...")
    return True  # Simulando um login bem-sucedido

# Função para exibir o painel principal após login
def painel_principal():
    while True:
        limpar_tela()
        linha()
        print("         📚 PAINEL PRINCIPAL 📚          ")
        linha()
        print("1️⃣ Visualizar Cursos Disponíveis")
        print("2️⃣ Meus Cursos")
        print("3️⃣ Sair\n")
        escolha = input("🔹 Escolha uma opção: ")

        if escolha == "1":
            cursos_disponiveis()
        elif escolha == "2":
            meus_cursos()
        elif escolha == "3":
            break
        else:
            input("\n❌ Opção inválida! Pressione ENTER para tentar novamente...")

# Função para exibir cursos disponíveis
def cursos_disponiveis():
    while True:
        limpar_tela()
        linha()
        print("      📜 LISTA DE CURSOS DISPONÍVEIS      ")
        linha()
        print("1️⃣ 🔹 Introdução à Programação")
        print("2️⃣ 🔹 Banco de Dados Avançado")
        print("3️⃣ 🔹 Machine Learning Básico")
        print("0️⃣ 🔙 Voltar\n")
        escolha = input("🔹 Escolha um curso para se inscrever: ")

        if escolha in ["1", "2", "3"]:
            print("\n✅ Inscrição realizada com sucesso!\n")
            input("🔹 Pressione ENTER para continuar...")
        elif escolha == "0":
            break
        else:
            input("\n❌ Opção inválida! Pressione ENTER para tentar novamente...")

# Função para exibir cursos do usuário
def meus_cursos():
    while True:
        limpar_tela()
        linha()
        print("          📂 MEUS CURSOS INSCRITOS       ")
        linha()
        print("1️⃣ 🎓 Introdução à Programação")
        print("0️⃣ 🔙 Voltar\n")
        escolha = input("🔹 Escolha um curso para acessar: ")

        if escolha == "1":
            acessar_curso()
        elif escolha == "0":
            break
        else:
            input("\n❌ Opção inválida! Pressione ENTER para tentar novamente...")

# Função para acessar um curso
def acessar_curso():
    while True:
        limpar_tela()
        linha()
        print("     📘 Introdução à Programação      ")
        linha()
        print("📌 Módulos disponíveis:")
        print("1️⃣ 🔹 Variáveis e Tipos de Dados")
        print("2️⃣ 🔹 Estruturas Condicionais")
        print("3️⃣ 🔹 Laços de Repetição")
        print("0️⃣ 🔙 Voltar\n")
        escolha = input("🔹 Escolha um módulo para estudar: ")

        if escolha in ["1", "2", "3"]:
            estudar_modulo()
        elif escolha == "0":
            break
        else:
            input("\n❌ Opção inválida! Pressione ENTER para tentar novamente...")

# Função para estudar um módulo do curso
def estudar_modulo():
    limpar_tela()
    linha()
    print("   ✏️ VARIÁVEIS E TIPOS DE DADOS   ")
    linha()
    print("📖 [Conteúdo do módulo exibido aqui...]\n")
    input("✅ Pressione ENTER para marcar como concluído e voltar...")

# Iniciar o sistema
menu_principal()