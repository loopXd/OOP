class minhaClasse:
    def __init__(self) -> None:
        self.__valor = None

    def setter_data(self, valor: int) -> None:
        self.__valor = valor
    
    def getter_data(self) -> int:
        return self.__valor

my_data = minhaClasse()
my_data.setter_data(23)
data = my_data.getter_data()

print(data)
