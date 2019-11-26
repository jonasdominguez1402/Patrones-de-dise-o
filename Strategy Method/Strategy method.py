#Metodo Strategy
"""
Patron de diseño Adapter

Jonathan Eliseo Dominguez Hdz

25/11/2019

En este ejemplo se prioriza el ataque de un pokemon al momento de atacar
se tienen estrategias de ataques y se utiliza la mas acertada
"""
from __future__ import annotations
from abc import ABC, abstractmethod
import random
import types


class Entrenador:
    
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy


    def efectividad(self,n) -> None:
 
        if n == 1:
            print(" super efectivo!!")
            
        else:
            print("Fallo!!")

        result = self._strategy.execute()

class Contrataque(ABC):
    @abstractmethod
    def execute(self):
        pass

class Ataque_uno(Contrataque):
    def execute(self):
        print("Lanzallamas")
    

class Ataque_dos(Contrataque):
    def execute(self):
       print("Furia dragon")
       

if __name__ == "__main__":
    context = Entrenador(Ataque_uno())
    
    print("El ataque de Charizard fue:")
    context.efectividad(1)
    print()

    print("El ataque de Charizard fue:")
    context.strategy = Ataque_dos()
    context.efectividad(2)
