class Select:
    def by_id(self):
        print("Selecionando um elemento no BD")

class Insert:
    def inser_value(self):
        print("Inserindo um valor no BD")

class Repository:
    def __init__(self):
        self.__select = Select() # COMPOSICAO
        self.__insert = Insert()

    def selectByID(self, id: int):
        self.__select.by_id()

repo = Repository()
repo.selectByID(341)
