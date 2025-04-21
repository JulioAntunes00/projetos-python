#Criando linhas para o menu
def linha(qtd=45):
    print("=" * qtd)


#Criando classes
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

#Criando um produto novo
p1 = Produto("Celular", 900.00)
p2 = Produto("Notebook", 2500.00)


#Mostrando informações do produto
print(f"{p1.nome} - R$, {p1.preco}")
print(f"{p2.nome} - R$, {p2.preco}")