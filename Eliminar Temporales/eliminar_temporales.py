import os
import shutil

def eliminar_archivos_temporales():
    # Obtener la ruta de la carpeta temporal del sistema
    carpeta_temp_sistema = os.getenv('TEMP')
    
    # Obtener la ruta de la carpeta temporal del usuario actual
    carpeta_temp_usuario = os.getenv('LOCALAPPDATA') + r'\Temp'
    
    carpetas_temp = [carpeta_temp_sistema, carpeta_temp_usuario]
    
    for carpeta in carpetas_temp:
        print(f"Eliminando archivos en {carpeta}...")
        if os.path.exists(carpeta):
            for archivo in os.listdir(carpeta):
                ruta_completa = os.path.join(carpeta, archivo)
                try:
                    # Verifica si es un archivo o carpeta y lo elimina
                    if os.path.isfile(ruta_completa) or os.path.islink(ruta_completa):
                        os.remove(ruta_completa)
                    elif os.path.isdir(ruta_completa):
                        shutil.rmtree(ruta_completa)
                    print(f"Eliminado: {ruta_completa}")
                except Exception as e:
                    print(f"Error eliminando {ruta_completa}: {e}")
        else:
            print(f"La carpeta {carpeta} no existe.")
        
        # Vuelve a crear la carpeta si fue completamente eliminada
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"Carpeta recreada: {carpeta}")

    print("Eliminación completada.")

if __name__ == "__main__":
    eliminar_archivos_temporales()
    input("Presiona Enter para salir...")