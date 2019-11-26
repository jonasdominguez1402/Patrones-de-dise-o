"""
Patron de diseño Adapter

Jonathan Eliseo Dominguez Hdz

25/11/2019
"""
from abc import ABC,abstractmethod

class IdiomaOficiales(ABC):

    @abstractmethod
    def lengua(self):
        pass

class Japones(IdiomaOficiales):
    def lengua(self):
        print("Hojayo!!")


class Ingles(IdiomaOficiales):
    def lengua(self):
        print("Hello!!")

class Otomi:
    def lengua(self):
        print("hats'i")

class IdiomaAdapter(IdiomaOficiales):

    def __init__(self):
        self._otomi = Otomi()

    def lengua(self):
        print("hats'i")

class IdiomasMundo:
    def __init__(self):
        self.japon = Japones()
        self.usa = Ingles()
        self.mexico = IdiomaAdapter()
        self.japon.lengua()
        self.usa.lengua()
        self.mexico.lengua()

Global = IdiomasMundo()
