import os

cursos_disponiveis_lista = {
    "1": "Introdução à Programação",
    "2": "Banco de Dados Avançado",
    "3": "Machine Learning Básico"
}
cursos_inscritos = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def linha(tamanho=45):
    print("=" * tamanho)

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

def fazer_login():
    limpar_tela()
    linha()
    print("               🔑 LOGIN                ")
    linha()
    email = input("📧 E-mail: ")
    senha = input("🔒 Senha: ")
    print("\n✅ Login realizado com sucesso!\n")
    input("🔹 Pressione ENTER para acessar o painel...")
    return True

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

def cursos_disponiveis():
    while True:
        limpar_tela()
        linha()
        print("      📜 LISTA DE CURSOS DISPONÍVEIS      ")
        linha()
        for key, value in cursos_disponiveis_lista.items():
            print(f"{key}️⃣ 🔹 {value}")
        print("0️⃣ 🔙 Voltar\n")
        escolha = input("🔹 Escolha um curso para se inscrever: ")

        if escolha in cursos_disponiveis_lista:
            curso = cursos_disponiveis_lista[escolha]
            if curso not in cursos_inscritos:
                cursos_inscritos.append(curso)
                print(f"\n✅ Inscrição no curso '{curso}' realizada com sucesso!\n")
            else:
                print(f"\n⚠️ Você já está inscrito no curso '{curso}'.\n")
            input("🔹 Pressione ENTER para continuar...")
        elif escolha == "0":
            break
        else:
            input("\n❌ Opção inválida! Pressione ENTER para tentar novamente...")

def meus_cursos():
    while True:
        limpar_tela()
        linha()
        print("          📂 MEUS CURSOS INSCRITOS       ")
        linha()
        if not cursos_inscritos:
            print("📭 Você ainda não está inscrito em nenhum curso.")
        else:
            for idx, curso in enumerate(cursos_inscritos, 1):
                print(f"{idx}️⃣ 🎓 {curso}")
        print("0️⃣ 🔙 Voltar\n")
        escolha = input("🔹 Escolha um curso para acessar: ")

        if escolha == "0":
            break
        elif escolha.isdigit() and 1 <= int(escolha) <= len(cursos_inscritos):
            acessar_curso(cursos_inscritos[int(escolha) - 1])
        else:
            input("\n❌ Opção inválida! Pressione ENTER para tentar novamente...")

def acessar_curso(nome_curso):
    while True:
        limpar_tela()
        linha()
        print(f"     📘 {nome_curso.upper()}      ")
        linha()
        print("📌 Módulos disponíveis:")
        print("1️⃣ 🔹 Variáveis e Tipos de Dados")
        print("2️⃣ 🔹 Estruturas Condicionais")
        print("3️⃣ 🔹 Laços de Repetição")
        print("0️⃣ 🔙 Voltar\n")
        escolha = input("🔹 Escolha um módulo para estudar: ")

        if escolha in ["1", "2", "3"]:
            estudar_modulo(escolha)
        elif escolha == "0":
            break
        else:
            input("\n❌ Opção inválida! Pressione ENTER para tentar novamente...")

def estudar_modulo(modulo):
    limpar_tela()
    linha()
    conteudos = {
        "1": """
✏️ VARIÁVEIS E TIPOS DE DADOS

📌 O que são variáveis?
Variáveis são espaços da memória onde guardamos dados.

📌 Exemplos:
    nome = "Ana"
    idade = 17
    altura = 1.65
    ativo = True

📌 Dica:
Use nomes simples e claros. Variáveis tornam seu código reutilizável!
""",

        "2": """
✏️ ESTRUTURAS CONDICIONAIS

📌 if/else
Permite tomar decisões no programa.

📌 Exemplo:
    idade = 18
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
""",

        "3": """
✏️ LAÇOS DE REPETIÇÃO

📌 for e while
Permitem repetir ações.

📌 Exemplo com for:
    for i in range(5):
        print(i)

📌 Exemplo com while:
    x = 0
    while x < 5:
        print(x)
        x += 1
"""
    }
    print(conteudos.get(modulo, "Conteúdo indisponível."))
    input("\n✅ Pressione ENTER para marcar como concluído e voltar...")

# Iniciar o sistema
menu_principal()
