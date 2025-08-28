import json

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

def carregar_tarefas(tarefas):
    with open("tarefas.json", "r") as arquivo:
        dados = json.load(arquivo)

def adicionar_tarefa(tarefas, descricao_nova_tarefa):
    nova_tarefa = {
        "descrição": descricao_nova_tarefa,
        "status": "pendente"
    }

    tarefas.append(nova_tarefa)
    print(f"Tarefa '{descricao_nova_tarefa}' adicionada com sucesso!")