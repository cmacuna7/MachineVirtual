# *******************************************************************************************************
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  
# Proposito:                      Generar Correos                                                    
# Autor:                          Marcelo Acuña
# Fecha de creacion:              17/12/2024                                                          
# Fecha de modificacion:          30/12/2024                                                          
# Materia:                        Estructura de datos                                                 
# NRC :                           1992                                                                
# *******************************************************************************************************

import os

def generar_correo(nombre, segundo_nombre, apellido):
    """
    Genera un correo basado en el nombre, segundo nombre y apellido.
    Si el correo ya existe en el archivo "personas.txt", se le agrega un contador al final.
    """
    # Convertir todo a minúsculas
    nombre_lower = nombre.lower()
    segundo_nombre_lower = segundo_nombre.lower()
    apellido_lower = apellido.lower()

    # Generar el correo base
    correo_base = f"{nombre_lower[0]}{segundo_nombre_lower[0]}{apellido_lower}@espe.edu.ec"
    correo_generado = correo_base

    # Verificar duplicados en el archivo personas.txt
    contador = 0
    if os.path.exists("personas.txt"):
        with open("personas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # Dividir la línea por ';' y obtener el correo en la posición esperada
                datos = linea.strip().split(';')
                if len(datos) >= 5:  # Verifica que haya al menos 5 columnas
                    correo_existente = datos[4]  # El correo está en la quinta posición
                    if correo_existente == correo_generado:
                        contador += 1
                        correo_generado = f"{correo_base.split('@')[0]}{contador}@espe.edu.ec"

    return correo_generado
