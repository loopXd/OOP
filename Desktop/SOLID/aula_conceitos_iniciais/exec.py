class pessoa():
    def __init__(self, altura, idade):
        print("inicial")
        self.altura = altura
        self.idade = idade
    def correr(self):
        print("Correr")
        print(self.altura)
        print(self.idade)
    def comer(self, extra):
        print("Comer")
        print(self.altura + extra)
        print(self.idade)
        
murilo = pessoa(1.80, 18)
murilo.comer(0.3)