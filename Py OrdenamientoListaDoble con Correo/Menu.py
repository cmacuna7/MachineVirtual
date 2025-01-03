# *******************************************************************************************************
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  
# Proposito:                      Menu                                                               
# Autor:                          Marcelo Acuña                  
# Fecha de creacion:              17/12/2024                                                          
# Fecha de modificacion:          30/12/2024                                                          
# Materia:                        Estructura de datos                                                  
# NRC :                           1992                                                                
# *******************************************************************************************************

import os
import time
import msvcrt  # Para capturar teclas en Windows
from BackupManager import BackupManager
from Utilidades import generar_correo
from Validaciones import Validaciones
from Persona import Persona
from Ayuda import mostrar_ayuda
from ListaDoble import ListaDoble
from Fecha import Fecha


def mostrar_menu(lista):
    opciones = [
        "Agregar persona",
        "Buscar persona",
        "Eliminar persona",
        "Ver todas las personas",
        "Crear backup",
        "Restaurar backup",
        "Ordenar por cédula",
        "Salir"
    ]
    seleccion_actual = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== Menú Principal ===")
        for i, opcion in enumerate(opciones):
            if i == seleccion_actual:
                print(f"> {opcion} <")
            else:
                print(f"  {opcion}")
        
        tecla = msvcrt.getch().decode("utf-8").lower()

        if tecla == "w":
            seleccion_actual = (seleccion_actual - 1) % len(opciones)
        elif tecla == "s":
            seleccion_actual = (seleccion_actual + 1) % len(opciones)
        elif tecla == "\r":  # Enter
            if opciones[seleccion_actual] == "Agregar persona":
                agregar_persona(lista)
            elif opciones[seleccion_actual] == "Buscar persona":
                buscar_persona(lista)
            elif opciones[seleccion_actual] == "Eliminar persona":
                eliminar_persona(lista)
            elif opciones[seleccion_actual] == "Ver todas las personas":
                lista.imprimir_personas()
                input("\nPresione Enter para volver al menú...")
            elif opciones[seleccion_actual] == "Crear backup":
                crear_backup(lista)
            elif opciones[seleccion_actual] == "Restaurar backup":
                BackupManager.restaurar_backup(lista)
            elif opciones[seleccion_actual] == "Ordenar por cédula":
                lista.ordenar_por_cedula()
                print("Lista ordenada por cédula.")
                input("\nPresione Enter para volver al menú...")
            elif opciones[seleccion_actual] == "Salir":
                print("Saliendo del programa...")
                break

def agregar_persona(lista):
    while True:
        print("\nPara salir, presione Enter sin ingresar nada en cualquier campo.")
        nombre = solicitar_dato("Ingrese Primer Nombre de la persona: ", Validaciones.validar_titulo_nombre, "Nombre")
        if nombre == "":
            return
        s_nombre = solicitar_dato("Ingrese Segundo Nombre de la persona: ", Validaciones.validar_titulo_nombre, "Segundo Nombre")
        if s_nombre == "":
            return
        apellido = solicitar_dato("Ingrese Apellido de la persona: ", Validaciones.validar_titulo_nombre, "Apellido")
        if apellido == "":
            return
        correo = generar_correo(nombre, s_nombre, apellido)
        print(f"El correo generado es: {correo}")
        cedula = solicitar_dato("Ingrese cédula: ", Validaciones.validar_cedula)
        if cedula == "":
            return
        fecha_nac_str = solicitar_dato("Ingrese fecha de nacimiento (DD-MM-YYYY): ", Validaciones.validar_fecha)
        if fecha_nac_str == "":
            return
        fecha_nac = Fecha.crear_desde_cadena(fecha_nac_str)
        
        persona = Persona(nombre, s_nombre, apellido, cedula, fecha_nac)
        lista.agregar_persona(persona)
        print("Persona agregada exitosamente.")
        input("\nPresione Enter para continuar...")

def buscar_persona(lista):
    while True:
        print("\nPara salir y regresar al menú, presione Enter sin ingresar nada.")
        cedula = input("Ingrese la cédula de la persona a buscar: ").strip()
        if cedula == "":
            return  # Regresa al menú principal
        nodo = lista.buscar_persona_por_cedula(cedula)
        if nodo:
            nodo.persona.mostrar()  # Call mostrar on the persona attribute
        else:
            print("Persona no encontrada.")
        input("\nPresione Enter para continuar...")

def eliminar_persona(lista):
    while True:
        print("\nPara salir, presione Enter sin ingresar nada.")
        cedula = input("Ingrese la cédula de la persona a eliminar: ").strip()
        if cedula == "":
            return
        if lista.eliminar_persona_por_cedula(cedula):
            print("Persona eliminada exitosamente.")
        else:
            print(f"Persona no encontrada con cédula: {cedula}.")
        input("\nPresione Enter para continuar...")

def crear_backup(lista):
    tiempo = time.localtime()
    nombre_backup = f"{tiempo.tm_year}_{tiempo.tm_mon}_{tiempo.tm_mday}_{tiempo.tm_hour}_{tiempo.tm_min}_{tiempo.tm_sec}.txt"
    lista.crear_backup(nombre_backup)
    print(f"Backup creado: {nombre_backup}")
    input("\nPresione Enter para continuar...")

def solicitar_dato(mensaje, validador, *args):
    while True:
        dato = input(mensaje).strip()
        if dato == "":
            return dato
        if validador(dato, *args):
            return dato
        print("Dato inválido. Intente nuevamente.")
