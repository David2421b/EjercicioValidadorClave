from abc import ABC, abstractmethod
from curses.ascii import isupper
from itertools import count


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self):
        pass

    def _validar_longitud(self, clave):
        count_1 = 0
        for i in clave:
            count_1 += 1

        if count_1 > self._longitud_esperada:
            return True

    def _contiene_mayuscula(self, clave):
        for item in clave:
            if item.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave):
        for item in clave:
            if item.islower():
                return True
        return False

    def _contiene_numero(self, clave):
        for item in clave:
            if item.isdigit():
                return True
        return False


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)


    def contiene_caracter_especial(self, clave):
        for item in clave:
            if item == "@" or "_" or "#" or "$" or "%":
                return True


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)

    def contiene_calisto(self):





