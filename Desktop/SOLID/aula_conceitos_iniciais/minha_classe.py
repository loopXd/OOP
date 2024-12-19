class MinhaClasse:
    def __init__(self, info, elem):
        print("Estou no construtor") # metodo construtor é o primeiro a exec
        self.atributo_1 = "Meu atributo"
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, "a"]
        self.atributo_novo = info

    def metodo_1(self):
        print(self.atributo_2)
        print("Minha acao1")
        print(self.atributo_novo)
        return "Ola Mundo"
    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_3[0] + numero)

# objeto        # classe -> instanciamos um objeto
minha_classe = MinhaClasse("Info", 213)

minha_classe.metodo_2(5)