class Animal:

    def andar(self) -> None:
        print("O Animal esta andando...")

class Mamifero(Animal):

    def mamar(self) -> None:
        print("O animal esta mamando...")

class Aves(Animal):

    def voar(self) -> None:
        print("O animal esta voando...")

class Cachorro(Mamifero):
    
    def latir(self) -> None:
        print("AU Au Au")
        self.andar()
        self.mamar()

class Passaro(Aves):
     
     def baterAsa(self):
        print("Batendo asa")
        self.andar()
        self.voar()

dog = Cachorro()
joaoDeBarro = Passaro()

dog.latir()
joaoDeBarro.baterAsa()
