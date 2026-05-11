import re
from abc import ABC, abstractmethod
from datetime import datetime

# --- 1. CLASE ABSTRACTA (Exigida por la guía) ---
class EntidadBase(ABC):
    def __init__(self, identificador):
        self.identificador = identificador

    @abstractmethod
    def mostrar_info(self):
        pass

# --- 2. EXCEPCIÓN PERSONALIZADA (Manejo robusto) ---
class ErrorDeValidacion(Exception):
    pass

# --- 3. CLASE CLIENTE (Encapsulación y validaciones estrictas) ---
class Cliente(EntidadBase):
    def __init__(self, cedula, nombre, correo, celular):
        super().__init__(cedula)
        self.__nombre = None
        self.__correo = None
        self.__celular = None
        
        # Estas asignaciones activan los setters de abajo
        self.nombre = nombre
        self.correo = correo
        self.celular = celular

    @property
    def nombre(self): return self.__nombre
    @nombre.setter
    def nombre(self, n):
        if len(n) < 3: raise ErrorDeValidacion(f"Nombre '{n}' muy corto.")
        self.__nombre = n

    @property
    def correo(self): return self.__correo
    @correo.setter
    def correo(self, c):
        if "@" not in c or "." not in c: raise ErrorDeValidacion(f"Email '{c}' inválido.")
        self.__correo = c

    @property
    def celular(self): return self.__celular
    @celular.setter
    def celular(self, cel):
        if not str(cel).isnumeric(): raise ErrorDeValidacion(f"Celular '{cel}' debe ser numérico.")
        self.__celular = cel

    def mostrar_info(self):
        return f"ID: {self.identificador} | Cliente: {self.nombre} | Email: {self.correo}"

# --- 4. REGISTRO DE LOGS (Registro de eventos y errores) ---
def registrar_log(mensaje):
    with open("log_software_fj.txt", "a", encoding="utf-8") as f:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{fecha}] ERROR: {mensaje}\n")

# --- 5. EJECUCIÓN DEL SISTEMA INTEGRAL ---
def ejecutar_sistema():
    # LISTA INTERNA (Toda la gestión se hace mediante listas, sin base de datos)
    lista_clientes_gestion = []

    # --- SIMULACIÓN DE 10 OPERACIONES (Obligatorio por la guía) ---
    print(">>> INICIANDO SIMULACIÓN DE 10 OPERACIONES (SOFTWARE FJ) <<<")
    
    operaciones_preparadas = [
        ("101", "Karol Malo", "karol@unad.edu.co", "3044051898"),   # 1. OK
        ("102", "Darwin", "darwin_error", "300123"),               # 2. FALLO
        ("103", "Victor", "victor@gmail.com", "CEL_LETRAS"),       # 3. FALLO
        ("104", "Nohemi", "nohemi@outlook.com", "3115556677"),     # 4. OK
        ("105", "Jhohiner", "jh", "3220001122"),                   # 5. FALLO
        ("106", "Darwin", "darwin@mail.com", "3009998877"),        # 6. OK
        ("107", "Vi", "vi@test.com", "3154443322"),                # 7. FALLO
        ("108", "Jhohiner", "jhohiner@unad.co", "3108889900"),     # 8. OK
        ("109", "Victor", "victor@mail.com", "3001112233"),        # 9. OK
        ("110", "Karol", "k@error", "000")                         # 10. FALLO
    ]

    for id_c, nom, mail, tel in operaciones_preparadas:
        try:
            nuevo = Cliente(id_c, nom, mail, tel)
            lista_clientes_gestion.append(nuevo)
            print(f"Simulación: Registro exitoso de {nom}")
        except ErrorDeValidacion as e:
            # Demuestra capacidad de continuar funcionando ante errores
            registrar_log(f"Simulación: {e}")
            print(f"Simulación: Error controlado en {nom}")

    print("\n--- SIMULACIÓN COMPLETADA ---")
    print(f"Estado del sistema: ESTABLE. Clientes en gestión: {len(lista_clientes_gestion)}\n")

    # --- GESTIÓN MANUAL (Parte integral de la tarea) ---
    while True:
        print("¿Deseas gestionar (registrar) un nuevo cliente manualmente?")
        op = input("Escribe 's' para registrar o 'n' para ver listado final y salir: ").strip().lower()

        if op == 's':
            print("\n--- NUEVO REGISTRO ---")
            id_m = input("Cédula: ")
            no_m = input("Nombre: ")
            co_m = input("Correo: ")
            te_m = input("Celular: ")

            try:
                # Bloque try/except/else/finally exigido
                cliente_nuevo = Cliente(id_m, no_m, co_m, te_m)
            except ErrorDeValidacion as e:
                print(f" ERROR: {e}")
                registrar_log(f"Manual: {e}")
            else:
                # Se ejecuta si NO hubo error
                lista_clientes_gestion.append(cliente_nuevo)
                print(" Cliente guardado en el sistema.")
            finally:
                # Se ejecuta SIEMPRE
                print("Proceso de registro finalizado. Sistema listo.\n")
        
        elif op == 'n':
            break

    # --- LISTADO FINAL (Demostración de gestión funcional) ---
    print("\n" + "="*55)
    print("LISTADO DE GESTIÓN FINAL - SOFTWARE FJ (SIN BASE DE DATOS)")
    print("="*55)
    for cliente in lista_clientes_gestion:
        print(cliente.mostrar_info())

if __name__ == "__main__":
    ejecutar_sistema()