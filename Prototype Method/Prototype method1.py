"""
Patron de diseño Prototype

Jonathan Eliseo Dominguez Hdz

25/11/2019
"""
import copy

class Prototype:

   _clonsombra = None
   _numero = None

   def clone(self):
      pass

   def getClonsombra(self):
      return self._clonsombra

   def getNumero(self):
      return self._numero
    

class Naruto(Prototype):

   def __init__(self, number):
      self._clonsombra = "Naruto"
      self._numero = number

   def clone(self):
      return copy.copy(self)

class Sasuke(Prototype):

   """ Concrete prototype. """

   def __init__(self, number):
      self._clonsombra = "Sasuke"
      self._numero = number

   def clone(self):
      return copy.copy(self)

class Ninjutsuclones:

   __narutonumero1 = None
   __narutonumero2 = None
   __sasukenumero1 = None
   __sasukenumero2 = None

   @staticmethod
   def initialize():
      Ninjutsuclones.__narutonumero1 = Naruto(1)
      Ninjutsuclones.__narutonumero2 = Naruto(2)
      Ninjutsuclones.__sasukenumero1 = Sasuke(1)
      Ninjutsuclones.__sasukenumero2 = Sasuke(2)

   @staticmethod
   def getNclondesombra1():
      return Ninjutsuclones.__narutonumero1.clone()

   @staticmethod
   def getNclondesombra2():
      return Ninjutsuclones.__narutonumero2.clone()

   @staticmethod
   def getSclondesombra1():
      return Ninjutsuclones.__sasukenumero1.clone()

   @staticmethod
   def getSclondesombra2():
      return Ninjutsuclones.__sasukenumero2.clone()

def main():
   Ninjutsuclones.initialize()
   
   instance = Ninjutsuclones.getNclondesombra1()
   print ("%s: %s" % (instance.getClonsombra(), instance.getNumero()))
   
   instance = Ninjutsuclones.getNclondesombra2()
   print ("%s: %s" % (instance.getClonsombra(), instance.getNumero()))
   
   instance = Ninjutsuclones.getSclondesombra1()
   print ("%s: %s" % (instance.getClonsombra(), instance.getNumero()))
   
   instance = Ninjutsuclones.getSclondesombra2()
   print ("%s: %s" % (instance.getClonsombra(), instance.getNumero()))

if __name__ == "__main__":
   main()
