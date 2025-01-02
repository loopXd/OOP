from elementos.interfaces.elemento_interface import ElementoInterface
from elementos.elemento import Elemento
from elementos.elemento2 import Elemento2

class Principal:
    def __init__(self, elem: ElementoInterface):
        self.__elem = elem
    
    def run(self):
        self.__elem.executar()
        print("Estou finaizando na classe pricipal")

elemento = Elemento2()

cl1 = Principal(elemento)
cl1.run()
