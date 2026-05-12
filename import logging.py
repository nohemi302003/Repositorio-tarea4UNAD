import logging

# Configuración básica del log
logging.basicConfig(
    filename="sistema_logs.log",   # Nombre del archivo donde se guardarán los registros
  level=logging.DEBUG,           # Nivel de detalle (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Funciones de apoyo para registrar eventos
def registrar_evento(mensaje):
    logging.info(mensaje)

def registrar_error(mensaje):
    logging.error(mensaje)

def registrar_advertencia(mensaje):
    logging.warning(mensaje)

def registrar_critico(mensaje):
    logging.critical(mensaje)
