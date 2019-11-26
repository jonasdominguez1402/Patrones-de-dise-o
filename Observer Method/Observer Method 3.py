
import abc

class Celular:

    def __init__(self):
        self._tiendas = set()
        self._estado_celular = None

    def attach(self, tienda):
        tienda._celular = self
        self._tiendas.add(tienda)

    def detach(self, tienda):
        tienda._celular = None
        self._tiendas.discard(tienda)

    def _notify(self):
        for tienda in self._tiendas:
            observer.update(self._estado_celular)

    @property
    def estado_celular(self):
        return self._estado_celular

    @estado_celular.setter
    def estado_celular(self, arg):
        self._estado_celular = arg
        self._notify()


class Tienda(metaclass=abc.ABCMeta):

    def __init__(self):
        self._celular = None
        self._celular = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class Comprador(Tienda):


    def update(self, arg):
        self._estado_tienda = arg

def main():
    celular = Celular()
    comprador = Comprador()
    celular.attach(comprador)
    celular._estado_celula = 123


if __name__ == "__main__":
    main()
