from abc import ABC, abstractmethod
from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

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

    def __init__(self, longitud_esperada=8):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, clave):
        especial = "@_#$%"
        for i in especial:
            if i in clave:
                return True
        return False

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError()
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError()
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError()

        return True


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self, longitud_esperada=6):
        super().__init__(longitud_esperada)

    def contiene_calisto(self, clave):
        if "calisto" in clave.lower():
            counter = 0
            for item in clave:
                if item in "CALISTO":
                    counter += 1

            if 2 <= counter < 7:
                return True
        return False

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError()

class Validador:

    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)

    def validar_clave(clave: str, reglas: list):
        for regla in reglas:
            validador = Validador(regla)
            try:
                if validador.es_valida(clave):
                    print(f"La clave es válida según la {regla.__class__.__name__}")
            except ValueError as e:
                print(f"Error: {regla.__class__.__name__}: {str(e)}")

