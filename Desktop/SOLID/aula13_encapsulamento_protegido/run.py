class Mamifero:
    def __init__(self, location: str) -> None:
        self.location = location   
        self._tamanho = 1.23
    
    def andar(self) -> None:
        print(f"O animal esta andando por {self.location}")

    def _dormir(self): # Metodo protegido. (acessivel por classes maes e filhos)
        print("O gato esta dormindo...")

class Gato(Mamifero):
    def __init__(self, location):
        super().__init__(location)

    def miar(self):
        print("O gato esta miando...")
        self.andar()
        self._dormir()
        print(self._tamanho)

cat = Gato("Brasil")
cat.miar()
cat._dormir() # Deveria dar erro / elementos protegidos não devem ser chamados por objetos
