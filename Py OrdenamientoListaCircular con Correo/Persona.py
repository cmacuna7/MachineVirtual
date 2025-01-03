# *******************************************************************************************************
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  
# Proposito:                      Código para Datos personales                                        
# Autor:                          Marcelo Acuña
# Fecha de creacion:              17/12/2024                                                          
# Fecha de modificacion:          30/12/2024                                                          
# Materia:                        Estructura de datos                                                 
# NRC :                           1992                                                                
# *******************************************************************************************************

from Utilidades import generar_correo
from Fecha import Fecha

class Persona:
    def __init__(self, nombre, segundo_nombre, apellido, cedula, fecha_nacimiento, correo=None):
        self.nombre = nombre
        self.segundo_nombre = segundo_nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = Fecha.crear_desde_cadena(fecha_nacimiento) if isinstance(fecha_nacimiento, str) else fecha_nacimiento
        self.correo = correo if correo else generar_correo(nombre, segundo_nombre, apellido)

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_segundo_nombre(self):
        return self.segundo_nombre

    def get_apellido(self):
        return self.apellido

    def get_cedula(self):
        return self.cedula

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_correo(self):
        return self.correo

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
        self.correo = generar_correo(self.nombre, self.segundo_nombre, self.apellido)

    def set_segundo_nombre(self, segundo_nombre):
        self.segundo_nombre = segundo_nombre
        self.correo = generar_correo(self.nombre, self.segundo_nombre, self.apellido)

    def set_apellido(self, apellido):
        self.apellido = apellido
        self.correo = generar_correo(self.nombre, self.segundo_nombre, self.apellido)

    def set_cedula(self, cedula):
        self.cedula = cedula

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    # Método para mostrar la información de la persona
    def mostrar(self):
        print(f"{'Primer Nombre':<20}{'Segundo Nombre':<20}{'Apellido':<15}{'Cedula':<20}{'Correo':<30}{'Fecha de Nacimiento':<30}")
        print("-" * 130)
        print(f"{self.nombre:<20}{self.segundo_nombre:<20}{self.apellido:<15}{self.cedula:<20}{self.correo:<30}{self.fecha_nacimiento.mostrar():<30}")
