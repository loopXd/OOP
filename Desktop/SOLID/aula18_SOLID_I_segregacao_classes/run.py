# SOLID - Segregação das interfaces

from abc import ABC, abstractmethod

class Trabalhador(ABC): # Interface

    @abstractmethod
    def trabalhar(self):
        pass
    
    @abstractmethod
    def irParaCasa(self):
        pass

    @abstractmethod
    def consultarBeneficios(self):
        pass

class TrabalhadorTemp(ABC): # Interface

    @abstractmethod
    def trabalhar(self):
        pass
    
    @abstractmethod
    def irParaCasa(self):
        pass

class Professor(Trabalhador):
    def trabalhar(self):
        print("O professor esta trabalhando")
    
    def irParaCasa(self):
        print("O porfessor esta indo para casa")
    
    def consultarBeneficios(self):
        print("Consultar beneficios CLT")

class ProfessorSubst(TrabalhadorTemp):
    def trabalhar(self):
        print("O professor substituto esta trabalhando")
    
    def irParaCasa(self):
        print("O professor substituto esta indo para casa")
 
