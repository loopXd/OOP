# SOLID 

# O pricipio aberto e fechado - diz que uma classe deve estar sempre aberta para espansao mas fechada para modificações

class Artista:

    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def apresentarShow(self):
        print(f"O {self.tipo} esta apresentando seu show")
    
class Circo:

    def apresentar(self, artista: Artista) -> None:
        artista.apresentarShow()
        print("Fimmm")

circo = Circo()
magico = Artista("Magico")
malabarista = Artista("Malabares")
circo.apresentar(malabarista)
