########################################################################################################
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  #
# Proposito:                      Lista Simple                                           #
# Autor:                          Marcelo Acuña                                                       #
# Fecha de creacion:              17/12/2024                                                          #
# Fecha de modificacion:          30/12/2024                                                          #
# Materia:                        Estructura de datos                                                 #
# NRC :                           1992                                                                #
########################################################################################################

import os
from datetime import datetime
from Persona import Persona

class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    @staticmethod
    def crear_desde_cadena(fecha_str):
        dia, mes, anio = map(int, fecha_str.split('-'))
        return Fecha(dia, mes, anio)

    def mostrar(self):
        return f"{self.dia:02d}-{self.mes:02d}-{self.anio}"



class Nodo:
    def __init__(self, persona):
        self.persona = persona
        self.siguiente = None

class ListaSimple:
    def __init__(self, archivo_personas="personas.txt"):
        self.cabeza = None
        self.archivo_personas = archivo_personas
        self.evitar_guardar = False

    def agregar_persona(self, Persona):
        if self.buscar_persona_por_cedula(Persona.get_cedula()):
            print(f"Error: La cédula {Persona.get_cedula()} ya existe.")
            return

        nuevo = Nodo(Persona)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

        print(f"Persona agregada: {Persona.get_nombre()}")
        if not self.evitar_guardar:
            self.guardar_personas_en_archivo()

    def limpiar_lista(self):
        self.cabeza = None

    def imprimir_personas(self):
        if not self.cabeza:
            print("No hay personas registradas.")
            return

        print(f"{'Primer Nombre':<20}{'Segundo Nombre':<20}{'Apellido':<15}{'Cédula':<20}{'Correo':<30}{'Fecha de Nacimiento':<30}")
        print("-" * 130)
        actual = self.cabeza
        while actual:
            Persona = actual.persona
            print(f"{Persona.nombre:<20}{Persona.segundo_nombre:<20}{Persona.apellido:<15}{Persona.cedula:<20}{Persona.correo:<30}{Persona.fecha_nacimiento.mostrar():<30}")
            actual = actual.siguiente

    def buscar_persona(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.persona.get_nombre() == nombre:
                return actual
            actual = actual.siguiente
        return None

    def buscar_persona_por_cedula(self, cedula):
        actual = self.cabeza
        while actual:
            if actual.persona.get_cedula() == cedula:
                return actual
            actual = actual.siguiente
        return None

    def eliminar_persona_por_cedula(self, cedula):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.persona.get_cedula() == cedula:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"Persona eliminada: {cedula}")
                self.guardar_personas_en_archivo()
                return True
            anterior = actual
            actual = actual.siguiente
        print(f"Persona no encontrada: {cedula}")
        return False

    def guardar_personas_en_archivo(self):
        with open(self.archivo_personas, "w", encoding="utf-8") as archivo:
            actual = self.cabeza
            while actual:
                persona = actual.persona
                archivo.write(f"{persona.nombre};{persona.segundo_nombre};{persona.apellido};{persona.cedula};{persona.correo};{persona.fecha_nacimiento.mostrar()}\n")
                actual = actual.siguiente
        print(f"Personas guardadas en el archivo: {self.archivo_personas}")

    def cargar_personas_desde_archivo(self):
        if not os.path.exists(self.archivo_personas):
            print("No se encontró el archivo para cargar personas.")
            return

        with open(self.archivo_personas, "r") as archivo:
            for linea in archivo:
                nombre, segundo_nombre, apellido, cedula, correo, fecha_nac_str = linea.strip().split(";")
                fecha_nac = Fecha.crear_desde_cadena(fecha_nac_str.replace("/", "-"))  # Replace '/' with '-'
                persona = Persona(nombre, segundo_nombre, apellido, cedula, fecha_nac, correo)
                self.agregar_persona(persona)
        print("Personas cargadas desde el archivo.")

    def crear_backup(self, nombre_archivo):
        os.makedirs("backup", exist_ok=True)
        ruta_backup = os.path.join("backup", nombre_archivo)
        with open(ruta_backup, "w") as archivo:
            actual = self.cabeza
            while actual:
                persona = actual.persona
                archivo.write(f"{persona.nombre};{persona.segundo_nombre};{persona.apellido};{persona.cedula};{persona.correo};{persona.fecha_nacimiento.mostrar()}\n")
                actual = actual.siguiente
        print(f"Backup creado en: {ruta_backup}")

    def restaurarBackup(self, nombre_archivo):
        if not os.path.exists(nombre_archivo):
            print(f"No se encontró el archivo de backup: {nombre_archivo}")
            return

        print(f"Restaurando desde backup: {nombre_archivo}")
        self.limpiar_lista()
        self.evitar_guardar = True
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                nombre, segundo_nombre, apellido, cedula, correo, fecha_nac_str = linea.strip().split(";")
                fecha_nac = Fecha.crear_desde_cadena(fecha_nac_str)
                persona = Persona(nombre, segundo_nombre, apellido, cedula, fecha_nac, correo)
                self.agregar_persona(persona)
        self.evitar_guardar = False
        self.guardar_personas_en_archivo()

    def ordenar_por_cedula(self):
        personas = []
        actual = self.cabeza
        while actual:
            personas.append(actual.persona)
            actual = actual.siguiente

        personas.sort(key=lambda p: p.get_cedula())
        self.limpiar_lista()
        for persona in personas:
            self.agregar_persona(persona)
        self.guardar_personas_en_archivo()
