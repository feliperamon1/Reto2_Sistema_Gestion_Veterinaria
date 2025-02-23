from abc import ABC, abstractmethod
from datetime import datetime

# Clase base abstracta para representar a una persona (cliente de la veterinaria)
class Persona(ABC):  
    pass

# Clase base abstracta para representar a una mascota registrada en la veterinaria
class Mascota(ABC): 
    pass

# Clase base abstracta para representar una cita médica para una mascota
class Cita(ABC):
    pass

# Clase concreta que representa a un cliente de la veterinaria
class Cliente(Persona):
    pass

# Clase concreta para el registro de una mascota en el sistema
class RegistroMascota(Mascota):  # Clase concreta para representar el registro de una mascota
    pass

# Clase concreta que representa una cita médica de una mascota
class CitaMascota(Cita):
    pass

# Clase principal que administra el sistema de la veterinaria
class SistemaVeterinaria:

    # Función para registrar clientes
    def registrar_cliente(self):
        pass

    # Función para eliminar clientes         
    def eliminar_cliente(self):
        pass

    # Función para actualizar información del cliente
    def actualizar_cliente(self):
        pass

    # Función para registar mascota asociada al correspondiente cliente
    def registrar_mascota(self): 
        pass

    # Función para eliminar el registro de una mascota, ya sea por error en el registro o fallecimiento de la mascota
    def eliminar_mascota(self):
        pass

    # Función para actualizar información de las mascotas
    def actualizar_mascota(self):
        pass

    # Función para programar una cita
    def programar_cita(self):
        pass
    
    # Función para actualizar una cita
    def actualizar_cita(self):
        pass

    # Función para cancelar una cita de una mascota
    def cancelar_cita(self):
        pass

    # Función para consultar historial según una mascota específica
    def consultar_historial(self):
        pass

    # Función para buscar citas según una fecha específica
    def buscar_citas_por_fecha(self):
        pass

    # Función para generar un reporte de clientes con sus respectivas mascotas
    def generar_reporte_clientes(self):
        pass

    # While para crear opciones
    def iniciar(self):
        pass

# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.iniciar()