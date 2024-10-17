from validadorclave.modelo.validador import Validador, ReglaValidacionGanimedes, ReglaValidacionCalisto
from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError


def validar_clave(clave: str, reglas: list):
    for regla in reglas:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida según la {regla.__class__.__name__}")
        except NoCumpleLongitudMinimaError:
            print(f"Error: {regla.__class__.__name__}: La clave no cumple la longitud mínima.")
        except NoTieneLetraMayusculaError:
            print(f"Error: {regla.__class__.__name__}: La clave no tiene letra mayúscula.")
        except NoTieneLetraMinusculaError:
            print(f"Error: {regla.__class__.__name__}: La clave no tiene letra minúscula.")
        except NoTieneNumeroError:
            print(f"Error: {regla.__class__.__name__}: La clave no tiene un número.")
        except NoTieneCaracterEspecialError:
            print(f"Error: {regla.__class__.__name__}: La clave no tiene un caracter especial.")
        except NoTienePalabraSecretaError:
            print(f"Error: {regla.__class__.__name__}: La clave no contiene la palabra secreta 'calisto'.")
