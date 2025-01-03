# *******************************************************************************************************
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  
# Proposito:                      Validaciones                                                       
# Autor:                          Marcelo Acuña
# Fecha de creacion:              17/12/2024                                                          
# Fecha de modificacion:          30/12/2024                                                          
# Materia:                        Estructura de datos                                                 
# NRC :                           1992                                                                
# *******************************************************************************************************

import re
from datetime import datetime

class Validaciones:

    @staticmethod
    def validar_fecha(fecha: str) -> bool:
        """
        Valida una fecha en formato DD-MM-YYYY.
        """
        try:
            # Verificar formato
            if not re.match(r"\d{2}-\d{2}-\d{4}", fecha):
                print("Error: El formato de la fecha debe ser DD-MM-YYYY.")
                return False

            # Extraer día, mes y año
            dia, mes, anio = map(int, fecha.split("-"))

            # Validar límites de día, mes y año
            if anio <= 0 or mes < 1 or mes > 12 or dia < 1 or dia > Validaciones.dias_en_mes(mes, anio):
                print("Error: Fecha no válida.")
                return False

            # Comparar con la fecha actual
            fecha_actual = datetime.now()
            fecha_ingresada = datetime(anio, mes, dia)
            if fecha_ingresada > fecha_actual:
                print("Error: La fecha no puede ser mayor a la fecha actual.")
                return False

            return True
        except Exception:
            print("Error: Fecha no válida.")
            return False

    @staticmethod
    def validar_cedula(cedula: str) -> bool:
        """
        Valida una cédula ecuatoriana.
        """
        if len(cedula) != 10:
            print("Error: La cédula debe tener 10 dígitos.")
            return False

        try:
            provincia = int(cedula[:2])
            tercer_digito = int(cedula[2])

            if provincia < 1 or provincia > 24:
                print("Error: Los dos primeros dígitos deben corresponder a una provincia válida.")
                return False

            if tercer_digito >= 6:
                print("Error: El tercer dígito debe ser menor a 6.")
                return False

            suma = 0
            for i in range(9):
                digito = int(cedula[i])
                if i % 2 == 0:  # Posiciones pares (0, 2, ...)
                    digito *= 2
                    if digito > 9:
                        digito -= 9
                suma += digito

            digito_verificador = (10 - (suma % 10)) % 10
            if digito_verificador != int(cedula[9]):
                print("Error: La cédula no es válida.")
                return False

            return True
        except ValueError:
            print("Error: La cédula contiene caracteres no válidos.")
            return False

    @staticmethod
    def validar_texto_no_vacio(texto: str, campo: str) -> bool:
        """
        Valida que un texto no esté vacío o solo contenga espacios.
        """
        if not texto.strip():
            print(f"Error: El campo {campo} no puede estar vacío o contener solo espacios.")
            return False
        return True

    @staticmethod
    def validar_texto(texto: str, campo: str) -> bool:
        """
        Valida que un texto solo contenga letras y espacios válidos.
        """
        if not texto.strip():
            print(f"Error: El campo {campo} no puede estar vacío o contener solo espacios.")
            return False

        if not re.match(r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$", texto):
            print(f"Error: El campo {campo} solo debe contener letras, espacios y caracteres válidos en español.")
            return False

        return True

    @staticmethod
    def validar_titulo_nombre(texto: str, campo: str) -> bool:
        """
        Valida que un texto comience con mayúscula y no contenga espacios internos.
        """
        if not texto.strip():
            print(f"Error: El campo {campo} no puede estar vacío o contener solo espacios.")
            return False

        if not re.match(r"^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+$", texto):
            print(f"Error: El campo {campo} debe comenzar con una letra mayúscula y no contener espacios.")
            return False

        return True

    @staticmethod
    def dias_en_mes(mes: int, anio: int) -> int:
        """
        Retorna la cantidad de días en un mes para un año dado.
        """
        if mes in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif mes in {4, 6, 9, 11}:
            return 30
        elif mes == 2:
            return 29 if Validaciones.es_bisiesto(anio) else 28
        return 0

    @staticmethod
    def es_bisiesto(anio: int) -> bool:
        """
        Determina si un año es bisiesto.
        """
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
