class Aluno():
    def __init__(self, nome, curso, idade, mensalidade):
        self.nome = nome
        self.curso = curso
        self.idade = idade
        self.mensalidade = mensalidade
        
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Curso: {self.curso}")
        print(f"Idade: {self.idade}")
        print(f"Mensalidade: R${self.mensalidade:.2f}\n")
        
        
class AlunoBolsista(Aluno):
    def aplicar_desconto(self, porcentagem):
        desconto = self.mensalidade * (porcentagem/100)
        self.mensalidade -= desconto
        print(f"Desconto de {porcentagem}% aplicado!")
        print(f"Nova mensalidade de: {self.mensalidade:.2f}\n")
        
    
#Criando aluno 1
aluno1 = Aluno("Marcos", "ADM", 22, 450.00)
aluno1.mostrar_dados() #Mostrar dados do aluno

#Criando aluno 2
aluno2 = AlunoBolsista("André", "Psicologia", 19, 630.00) #Criando aluno com bolsa

aluno2.aplicar_desconto(50) #Aplicando desconto

aluno2.mostrar_dados()#Mostrar dados após o desconto