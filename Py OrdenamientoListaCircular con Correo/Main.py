# *******************************************************************************************************
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  
# Proposito:                      Programa Principal                                                  
# Autor:                          Marcelo Acuña                  
# Fecha de creacion:              17/12/2024                                                          
# Fecha de modificacion:          30/12/2024                                                          
# Materia:                        Estructura de datos                                                 
# NRC :                           1992                                                                
# *******************************************************************************************************

import os
import sys
from ListaCircular import ListaCircular
from Menu import mostrar_menu

# Configurar la consola para usar UTF-8 en sistemas Windows
if os.name == 'nt':
    import ctypes
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    ctypes.windll.kernel32.SetConsoleCP(65001)

class BackupManager:
    @staticmethod
    def crear_carpeta_si_no_existe(ruta):
        """Crea una carpeta si no existe"""
        if not os.path.exists(ruta):
            os.makedirs(ruta)

def main():
    # Crear carpeta de backups si no existe
    BackupManager.crear_carpeta_si_no_existe("backup")

    lista = ListaCircular()

    # Cargar las personas desde el archivo al iniciar
    try:
        lista.cargar_personas_desde_archivo()
    except ValueError as e:
        print(f"Error al cargar las personas desde el archivo: {e}", file=sys.stderr)
        return 1

    mostrar_menu(lista)
    return 0

if __name__ == "__main__":
    sys.exit(main())
