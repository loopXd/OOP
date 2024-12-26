#SOLID

#S - Responsabilidade Unica / Single Responsability

import erro

class sistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        if (self.__validate(nome, idade)):
            self.__register(nome, idade)
        else:
            self.__erro()
    
    def __validate(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int) #1
    
    def __register(self, nome: str, idade: int) -> None:
        print("Acessando banco de dados...") #2
        print(f"Cadastrar usuario {nome}, idade: {idade}")

    def __erro(self) -> None:
        print("Dados invalidos") #3

my_cadaster = sistemaCadastral()
my_cadaster.cadastrar("Murilo", "18")
