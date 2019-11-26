"""
Patron de diseño Facthory

Jonathan Eliseo Dominguez Hdz.

25/11/2019

"""

from abc import ABC, abstractmethod

class Peleadores(ABC):

    @abstractmethod
    def ataque(self):
        pass

class Goku(Peleadores):
    def ataque(self):
        return("Kame-Hame-Haaaa!!!")

class Piccolo(Peleadores):
    def ataque(self):
        return("Makanconsapo!!!")

class Vegeta(Peleadores):
    def ataque(self):
        return("Canoon Garlic!!!")

class WFactory:
    def Realizar_ataque(self, peleadores):
        return peleadores.ataque()

#Contraataque
class Contraataque:
    def __init__(self):
        self.factory = WFactory()
        print (self.factory.Realizar_ataque(Goku()))
        print (self.factory.Realizar_ataque(Piccolo()))
        print (self.factory.Realizar_ataque(Vegeta()))
c = Contraataque()
