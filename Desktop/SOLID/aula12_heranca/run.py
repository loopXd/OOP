class Mamifero:
    def __init__(self, location: str) -> None:
        self.location = location
    
    def andar(self) -> None:
        print(f"O animal esta andando por {self.location}")

class Cachorro(Mamifero):
    def __init__(self, location):
        super().__init__(location)
    
    def latir(self):
        print("O cachorro esta latindo...")
        self.andar()

class Gato(Mamifero):
    def __init__(self, location):
        super().__init__(location)

    def miar(self):
        print("O gato esta miando...")
        self.andar()

dog = Cachorro("Brasil")
dog.latir()

cat = Gato("Argentina")
cat.miar()
