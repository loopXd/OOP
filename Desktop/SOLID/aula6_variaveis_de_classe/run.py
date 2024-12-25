class minhaClasse:

    estatico = "Lhama" # uso de variavel estatica em php seria: static estatico = "Lhama"

    def __init__(self, estado) -> None:
        self.__estado = estado

obj1 = minhaClasse(True)
obj2 = minhaClasse(True)

minhaClasse.estatico = "Programador"
obj1.estatico = "Hello"
minhaClasse.estatico = "LhamaAqui"

print(obj1.estatico)
print(obj2.estatico)
print(minhaClasse.estatico)
