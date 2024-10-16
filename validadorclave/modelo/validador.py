from abc import ABC, abstractmethod
from itertools import count


class ReglaValidacion(ABC):

    def __init__(self, longitu_esperada: int):
        self._longitud_esperada: int = longitu_esperada

    @abstractmethod
    def es_valida(self):
        pass

    def _validar_longitud(self, clave):
        count = 0
        for i in clave:
            count += 1

        if count > self._longitud_esperada:
            return True

    def _contiene_mayuscula(self):
        pass

    def _contiene_minuscula(self):
        pass

    def _contiene_numero(self):
        pass