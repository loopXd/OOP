class minha_classe:
    def __init__(self, info): # metodo construtor
        self.atribute1 = "minha classe"
        self.atribute2 = [1, 2, "a"]
        self.atribute3 = info
        print(self.atribute3)

    def metodo1(self):
        print("minha acao 1")
    
    def metodo2(self):
        print("minha acao 2")
        return "ola mundo"

#objeto        #classe > instaciamos um objeto
minha_classe = minha_classe(123)

reponse = minha_classe.metodo2()
print(reponse)