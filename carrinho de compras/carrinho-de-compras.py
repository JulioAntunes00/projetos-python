#Classe que representa um produto com nome e preço
class Produtos:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

#Classe que representa o carrinho de compras
class Carrinho:
    def __init__(self):
        self.itens = [] #lista para armazenar os produtos adicionados

    #metodo para adicionar um produto ao carrinho
    def add_carrinho(self, add_item):
        self.itens.append(add_item)

    #metodo para mostrar todos itens do carrinho
    def mostrar_itens(self):
        if not self.itens:
            print("O carrinho está vazio")
        else:
            print("Produtos no carrinho: ")
            for produto in self.itens:
                print(f" - {produto.nome} - R$ {produto.preço:.2f}")
            
    #metodo para calcular o valor total do carrinho
    def calcular_total(self):
        total = 0
        for produto in self.itens:
            total += produto.preço
        print(f"\n Total da compra: R$ {total:.2f}")

#Criando produtos
p1 = Produtos("iphone", 999.00)
p2 = Produtos("Notebook", 1500.00)
p3 = Produtos("Impressora", 800.00)

#criando carrinho
carrinho = Carrinho()

#Adicionar produtos
carrinho.add_carrinho(p1)
carrinho.add_carrinho(p2)
carrinho.add_carrinho(p3)

#mostrar o que tem no carrinho
carrinho.mostrar_itens()

#exibir valor total do carrinho
carrinho.calcular_total()
