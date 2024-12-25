class minhaClasse:

    estatico = "Lhama" # uso de variavel estatica em php seria: static estatico = "Lhama"

    def __init__(self, estado) -> None:
        self.__estado = estado
        
    @classmethod
    def alteracao_da_variavel_classe(cls):
        cls.estatico = "AlgumaCoisa"
        # minhaClasse.estatico = "AlgumaCoisa"

obj1 = minhaClasse(True)
obj2 = minhaClasse(True)

obj1.alteracao_da_variavel_classe()

print(obj1.estatico)
print(obj2.estatico)
print(minhaClasse.estatico)
