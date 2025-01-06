########################################################################################################
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  #
# Proposito:                      Lista Circular                                            #
# Autor:                          Marcelo Acuña                                                       #
# Fecha de creacion:              17/12/2024                                                          #
# Fecha de modificacion:          30/12/2024                                                          #
# Materia:                        Estructura de datos                                                 #
# NRC :                           1992                                                                #
########################################################################################################

import os
from datetime import datetime
from Persona import Persona
from Nodo import Nodo
from Fecha import Fecha
from BackupManager import BackupManager

class ListaCircular:
    def __init__(self, archivo_personas="personas.txt"):
        self.cabeza = None
        self.archivo_personas = archivo_personas
        self.evitar_guardar = False

    def agregar_persona(self, persona):
        if self.buscar_persona_por_cedula(persona.get_cedula()):
            print(f"Error: La cédula {persona.get_cedula()} ya existe.")
            return

        nuevo = Nodo(persona)
        if not self.cabeza:
            self.cabeza = nuevo
            self.cabeza.siguiente = self.cabeza  # Hacer circular
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza  # Hacer circular

        print(f"Persona agregada: {persona.get_nombre()}")
        if not self.evitar_guardar:
            self.guardar_personas_en_archivo()

    def limpiar_lista(self):
        if not self.cabeza:
            return
        actual = self.cabeza
        while True:
            siguiente = actual.siguiente
            if siguiente == self.cabeza:
                break
            del actual
            actual = siguiente
        self.cabeza = None

    def imprimir_personas(self):
        if not self.cabeza:
            print("No hay personas registradas.")
            return

        print(f"{'Primer Nombre':<20}{'Segundo Nombre':<20}{'Apellido':<15}{'Cédula':<20}{'Correo':<30}{'Fecha de Nacimiento':<30}")
        print("-" * 130)
        actual = self.cabeza
        while True:
            persona = actual.persona
            print(f"{persona.nombre:<20}{persona.segundo_nombre:<20}{persona.apellido:<15}{persona.cedula:<20}{persona.correo:<30}{persona.fecha_nacimiento.mostrar():<30}")
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def buscar_persona(self, nombre):
        if not self.cabeza:
            return None
        actual = self.cabeza
        while True:
            if actual.persona.get_nombre() == nombre:
                return actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return None

    def buscar_persona_por_cedula(self, cedula):
        if not self.cabeza:
            return None
        actual = self.cabeza
        while True:
            if actual.persona.get_cedula() == cedula:
                return actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return None

    def eliminar_persona_por_cedula(self, cedula):
        if not self.cabeza:
            return False
        actual = self.cabeza
        anterior = None
        while True:
            if actual.persona.get_cedula() == cedula:
                if actual == self.cabeza and actual.siguiente == self.cabeza:
                    # Case when there is only one node in the list
                    self.cabeza = None
                elif actual == self.cabeza:
                    # Case when the node to be deleted is the head node
                    temp = self.cabeza
                    while temp.siguiente != self.cabeza:
                        temp = temp.siguiente
                    self.cabeza = actual.siguiente
                    temp.siguiente = self.cabeza
                else:
                    anterior.siguiente = actual.siguiente
                del actual
                print(f"Persona eliminada: {cedula}")
                self.guardar_personas_en_archivo()
                return True
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print(f"Persona no encontrada: {cedula}")
        return False

    def guardar_personas_en_archivo(self):
        with open(self.archivo_personas, "w", encoding="utf-8") as archivo:
            if not self.cabeza:
                return
            actual = self.cabeza
            while True:
                persona = actual.persona
                archivo.write(f"{persona.nombre};{persona.segundo_nombre};{persona.apellido};{persona.cedula};{persona.correo};{persona.fecha_nacimiento.mostrar()}\n")
                actual = actual.siguiente
                if actual == self.cabeza:
                    break
        print(f"Personas guardadas en el archivo: {self.archivo_personas}")

    def cargar_personas_desde_archivo(self):
        if not os.path.exists(self.archivo_personas):
            print("No se encontró el archivo para cargar personas.")
            return

        with open(self.archivo_personas, "r") as archivo:
            for linea in archivo:
                nombre, segundo_nombre, apellido, cedula, correo, fecha_nac_str = linea.strip().split(";")
                fecha_nac = Fecha.crear_desde_cadena(fecha_nac_str.replace("/", "-"))
                persona = Persona(nombre, segundo_nombre, apellido, cedula, fecha_nac, correo)
                self.agregar_persona(persona)
        print("Personas cargadas desde el archivo.")

    def crear_backup(self, nombre_archivo):
        os.makedirs("backup", exist_ok=True)
        ruta_backup = os.path.join("backup", nombre_archivo)
        with open(ruta_backup, "w") as archivo:
            if not self.cabeza:
                return
            actual = self.cabeza
            while True:
                persona = actual.persona
                archivo.write(f"{persona.nombre};{persona.segundo_nombre};{persona.apellido};{persona.cedula};{persona.correo};{persona.fecha_nacimiento.mostrar()}\n")
                actual = actual.siguiente
                if actual == self.cabeza:
                    break
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
        if not self.cabeza:
            return
        actual = self.cabeza
        while True:
            personas.append(actual.persona)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        personas.sort(key=lambda p: p.get_cedula())
        self.limpiar_lista()
        for persona in personas:
            self.agregar_persona(persona)
        self.guardar_personas_en_archivo()
