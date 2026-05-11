# =========================================
# EXCEPCIONES PERSONALIZADAS

import logging

# =========================================
# CONFIGURACIÓN DE LOGS
# =========================================

logging.basicConfig(
    filename='./errores_sistema.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# =========================================
# EXCEPCIONES DE CLIENTES
# =========================================

class ClienteError(Exception):
    pass


class NombreInvalidoError(ClienteError):
    pass


class CorreoInvalidoError(ClienteError):
    pass


class CelularInvalidoError(ClienteError):
    pass


# =========================================
# EXCEPCIONES DE SERVICIOS
# =========================================

class ServicioError(Exception):
    pass


class NochesInvalidasError(ServicioError):
    pass


class DistanciaInvalidaError(ServicioError):
    pass


class ExcesoPersonasError(ServicioError):
    pass


# =========================================
# EXCEPCIONES DE RESERVAS
# =========================================

class ReservaError(Exception):
    pass


class ReservaDuplicadaError(ReservaError):
    pass


class FechaInvalidaError(ReservaError):
    pass


class HorarioNoDisponibleError(ReservaError):
    pass


class ClienteNoEncontradoError(ReservaError):
    pass


class ServicioNoDisponibleError(ReservaError):
    pass


# =========================================
# FUNCIÓN PARA REGISTRAR ERRORES
# =========================================

def registrar_log(mensaje):
    logging.error(mensaje)


# =========================================
# PRUEBA GENERAL DEL SISTEMA
# =========================================

if __name__ == "__main__":

    # ----- CLIENTES -----
    try:
        raise NombreInvalidoError(
            "El nombre es demasiado corto"
        )

    except ClienteError as e:
        print("ERROR DE CLIENTE:", e)
        registrar_log(e)

    # ----- SERVICIOS -----
    try:
        raise NochesInvalidasError(
            "Cantidad de noches inválida"
        )

    except ServicioError as e:
        print("ERROR DE SERVICIO:", e)
        registrar_log(e)

    # ----- RESERVAS -----
    try:
        raise FechaInvalidaError(
            "La fecha ingresada no es válida"
        )

    except ReservaError as e:
        print("ERROR DE RESERVA:", e)
        registrar_log(e)

    finally:
        print("\nSistema de excepciones funcionando correctamente.")