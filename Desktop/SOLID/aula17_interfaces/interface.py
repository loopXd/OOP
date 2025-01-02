from abc import ABC, abstractmethod

class Trabalhador(ABC): # Interface

    @abstractmethod
    def trabalhar(self):
        pass
    
    @abstractmethod
    def irParaCasa(self):
        pass

    @abstractmethod
    def horarioDeAlmoco(self):
        pass