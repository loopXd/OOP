class BancoDeDados:

    def __init__(self, nome: str, idade: str) -> None:
        self.nome = nome
        self.idade = idade 

    def registro(self):
        print(f"Usuario {self.nome} com idade {self.idade} registrado")
    
    def excluir(self):
        print(f"Usuario {self.nome} com idade {self.idade} excluido")

class Pessoa:

    def incluirRegistro(self, bancoDeDados: BancoDeDados):
        bancoDeDados.registro()

    def excluirRegistro(self, bancoDeDados: BancoDeDados):
        bancoDeDados.excluir()

    def consultarBancoDeDados(self, bancoDeDados: BancoDeDados):
        print(f"Esses sao os usuarios: {bancoDeDados.nome} e sua respectiva idade {bancoDeDados.idade}")

murilo = Pessoa()
register = BancoDeDados("Murilo", 18)
register2 = BancoDeDados("Caio", 14)
murilo.incluirRegistro(register)
murilo.consultarBancoDeDados(register2)
