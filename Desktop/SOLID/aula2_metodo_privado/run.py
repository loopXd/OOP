class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf

    def apresentar(self):
        print(f'Ola, minha altura - {self.altura}')
        self.__coletar_documento()
    
    def __coletar_documento(self):
        print(f'Meu documento - {self.__cpf}')

murilo = Pessoa("1.70", "16177018742")
murilo.apresentar()
