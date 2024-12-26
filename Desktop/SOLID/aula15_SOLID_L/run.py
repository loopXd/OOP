# Substituição de Liskov - SOLID
# QUebrando a regra
class Animal:
    def alimentar(self):
        print("O animal esta se alimentando...")

class Cachorro(Animal):
    def latir(self):
        print("O cachorro esta latindo...")

class Peixe(Cachorro):
    def nadar(self):
        print("O peixe esta nadando...")
     
    def latir(self): # Comportamento diferente
        print("O Peixe esta latindo...") 
