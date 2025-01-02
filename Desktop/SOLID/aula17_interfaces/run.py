from interface import Trabalhador

class Professor(Trabalhador): # Implementação da interface
    def trabalhar(self):
        print("O professor esta trabalhando")
    
    def irParaCasa(self):
        print("O porfessor esta indo para casa")
    
    def horarioDeAlmoco(self):
        print("O porfessor esta almoçando")

class Engenheiro(Trabalhador): # Implementação da interface
    def trabalhar(self):
        print("O Engenheiro esta trabalhando")
    
    def irParaCasa(self):
        print("O Engenheiro esta indo para casa")
    
    def horarioDeAlmoco(self):
        print("O Engenheiro esta almoçando")

def comunicarTrabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print("Comunicar o trabalhador para ir para casa")
    trabalhador.irParaCasa()

p1 = Professor()
p2 = Engenheiro()

comunicarTrabalhador(p1)
print()
comunicarTrabalhador(p2)
