from abc import ABC, abstractmethod


class ReglaValidacion(ABC):

    def _init_(self, longitud_esperada):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
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

    def _init_(self, longitud_esperada):
        super()._init_(longitud_esperada=8)

    def contiene_caracter_especial(self, clave):
        counter = 0
        for item in clave:
            if item == "@" or "_" or "#" or "$" or "%":
                counter += 1

            if counter >= 1:
                return True
            else:
                return False

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise ValueError("NoCumpleLongitudMinimaError")
        if not self._contiene_mayuscula(clave):
            raise ValueError("NoTieneLetraMayusculaError")
        if not self._contiene_minuscula(clave):
            raise ValueError("NoTieneLetraMinusculaError")
        if not self._contiene_numero(clave):
            raise ValueError("NoTieneNumeroError")
        if not self.contiene_caracter_especial(clave):
            raise ValueError("NoTieneCaracterEspecialError")

        return True


class ReglaValidacionCalisto(ReglaValidacion):

    def _init_(self, longitud_esperada):
        super()._init_(longitud_esperada=6)

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
            raise ValueError("NoCumpleLongitudMinimaError")
        if not self._contiene_numero(clave):
            raise ValueError("NoTieneNumeroError")
        if not self.contiene_calisto(clave):
            raise ValueError("NoTienePalabraSecretaError")

class Validador:

    def _init_(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)

    def validar_calve(clave: str, reglas: list):
        for regla in reglas:
            validador = Validador(clave)
            pass

