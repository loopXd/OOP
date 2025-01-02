from Imine import Bloco

class Madeira(Bloco):
    def tipo(self, tipo: str):
        self.tipo = tipo

    def colocarBloco(self):
        print(f"Colocando bloco {self.tipo}")

bloco1 = Madeira()
bloco1.tipo("Madeira")
bloco1.colocarBloco()
