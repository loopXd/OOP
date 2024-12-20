class minhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        self.__elem = None
    
    def setter_valor(self, valor: int) -> None:
        self.__valor = valor

    def getter_valor(self) -> int:
        return self.__valor

my_class = minhaClasse()
#my_class.valor = 3 # ferindo o encapsulamento

my_class.setter_valor(input("Passe um valor "))
valor = my_class.getter_valor()

print(valor)
