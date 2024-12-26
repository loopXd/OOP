from abc import ABC, abstractmethod

class Pessoa(ABC): # CLasse abstrata não possui objetos - so pode ser mae (heranca)
    def correr(self) -> None:
        print("A pessoa esta correndo de manha")
    
    @abstractmethod # Classe filha DEVE criar um metodo trabalhar
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print("O professor esta dando aula...")

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print("O cozinheiro esta cozinhando...")

p1 = Professor() # daria erro
c1 = Cozinheiro()

c1.trabalhar()

p1.trabalhar()
p1.correr()
