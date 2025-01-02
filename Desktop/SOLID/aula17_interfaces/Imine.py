from abc import ABC, abstractmethod

class Bloco:
    @abstractmethod
    def tipo(self, tipo: str) -> None:
        self.tipo = tipo
    
    @abstractmethod
    def colocarBloco(self):
        print(f"Colocando bloco {self.tipo}")

madeira = Bloco("Madeira")
pedra = Bloco("Pedra")
tnt = Bloco("TNT")

madeira.colocarBloco()
tnt.colocarBloco()
pedra.colocarBloco()
