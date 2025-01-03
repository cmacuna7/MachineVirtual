########################################################################################################
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  #
# Proposito:                      Ayuda para manejar el sistema                                       #
# Autor:                          Marcelo Acuña                                                       #
# Fecha de creacion:              17/12/2024                                                          #
# Fecha de modificacion:          30/12/2024                                                          #
# Materia:                        Estructura de datos                                                 #
# NRC :                           1992                                                                #
########################################################################################################

import os

def mostrar_ayuda():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Encabezado
    print("=======================================")
    print("              Uso Básico              ")
    print("=======================================")

    # Sección de uso básico
    print("\n1. Registrar un libro:")
    print("   Para registrar un nuevo libro, seleccione la opción")
    print("   'Agregar libro' desde el menú principal. Ingrese los")
    print("   datos requeridos como título, autor, año de publicación")
    print("   y género, y haga clic en 'GUARDAR'.")

    print("\n2. Buscar un libro:")
    print("   Utilice la opción 'Buscar libro' e ingrese los parámetros")
    print("   de búsqueda (como título o autor) para encontrar un libro en el registro.")

    print("\n3. Eliminar un libro:")
    print("   Seleccione el libro que desea eliminar de la lista de libros")
    print("   y haga clic en 'ELIMINAR'. Confirme la acción para borrar el libro del registro.")

    print("\n4. Imprimir lista de libros:")
    print("   Puede imprimir la lista de libros registrados seleccionando")
    print("   la opción 'IMPRIMIR' en el menú principal.")

    # Separador
    print("\n=======================================")
    print("           Funciones Avanzadas         ")
    print("=======================================")

    # Sección de funciones avanzadas
    print("\n1. Realizar un Backup:")
    print("   Para realizar un backup de los datos, seleccione la")
    print("   opción 'BACKUP' desde el menú. El sistema guardará")
    print("   una copia de seguridad de los datos en formato de fecha y hora")
    print("   (año-mes-día-hora-minuto-segundo).")

    print("\n2. Restaurar desde un Backup:")
    print("   Para restaurar un backup, seleccione 'RESTAURAR BACKUP'")
    print("   desde el menú y elija el archivo de backup correspondiente.")
    print("   El sistema recuperará los datos a partir de esa copia de seguridad.")

    # Instrucción para continuar
    print("\n=======================================")
    print("Presione 'Enter' para continuar...")
    print("=======================================")

    # Pausa para el usuario
    input()
