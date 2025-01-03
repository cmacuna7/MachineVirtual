########################################################################################################
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  #
# Proposito:                      Backup para restaurar datos                                         #
# Autor:                          Marcelo Acuña                                                       #
# Fecha de creacion:              17/12/2024                                                          #
# Fecha de modificacion:          18/12/2024                                                          #
# Materia:                        Estructura de datos                                                 #
# NRC :                           1992                                                                #
########################################################################################################

import os
import shutil

class BackupManager:
    @staticmethod
    def crearCarpetaSiNoExiste(ruta):
        if not os.path.exists(ruta):
            try:
                os.makedirs(ruta)
                print(f"Carpeta creada: {ruta}")
            except OSError as e:
                print(f"Error al crear la carpeta: {ruta}. {e}")
        else:
            print(f"La carpeta ya existe: {ruta}")

    @staticmethod
    def listarArchivosEnCarpeta(carpeta):
        try:
            archivos = os.listdir(carpeta)
            return [archivo for archivo in archivos if os.path.isfile(os.path.join(carpeta, archivo))]
        except FileNotFoundError:
            print(f"Error al acceder a la carpeta: {carpeta}")
            return []

    @staticmethod
    def restaurar_backup(lista):
        carpeta_backup = "backup"  # Carpeta donde se almacenan los backups
        archivos = BackupManager.listarArchivosEnCarpeta(carpeta_backup)

        if not archivos:
            print(f"No se encontraron archivos de backup en la carpeta {carpeta_backup}.\n")
            return

        # Mostrar los archivos disponibles
        print("Archivos disponibles para restaurar:")
        for i, archivo in enumerate(archivos, start=1):
            print(f"{i}. {archivo}")

        # Seleccionar archivo
        try:
            seleccion = int(input("Seleccione un archivo para restaurar (ingrese el número): "))
            if seleccion < 1 or seleccion > len(archivos):
                print("Selección inválida.\n")
                return
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.\n")
            return

        archivo_seleccionado = os.path.join(carpeta_backup, archivos[seleccion - 1])
        lista.restaurarBackup(archivo_seleccionado)
