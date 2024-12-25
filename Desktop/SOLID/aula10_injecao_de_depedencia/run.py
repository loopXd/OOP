class Celular:
    def __init__(self, modelo: str):
        self.__modelo = modelo

    def enviarMensagem(self, mensagem: str):
        print(f"Enviando mensagem: {mensagem}")

    def enviarEmail(self):
        print("Enviando emails...")

    def abrirYoutube(self):
        print("Abrindo youtube...")

class Pessoa:
    def __init__(self, celular: Celular):
        self.__celular = celular
    
    def pedirPizza(self, sabor: str):
        self.sabor = sabor
        print("Buscando celular")
        self.__celular.enviarMensagem(f"Desejo o sabor: {self.sabor}")
    
    def estudar(self, materia: str):
        self.materia = materia
        print(f"Vamos estudar {self.materia}")
        self.__celular.abrirYoutube()

android = Celular("Samsung")
apple = Celular("Iphone")

murilo = Pessoa(apple)

murilo.pedirPizza("Calabresa")
murilo.estudar("Portugues")
