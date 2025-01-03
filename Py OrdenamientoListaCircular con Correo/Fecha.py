########################################################################################################
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  #
# Proposito:                      Fecha para clase persona                                            #
# Autor:                          Marcelo Acuña                                                       #
# Fecha de creacion:              17/12/2024                                                          #
# Fecha de modificacion:          30/12/2024                                                          #
# Materia:                        Estructura de datos                                                 #
# NRC :                           1992                                                                #
########################################################################################################

import datetime


class Fecha:
    def __init__(self, dia, mes, anio):
        if not self.es_fecha_valida(dia, mes, anio):
            raise ValueError("Fecha inválida")
        self.dia = dia
        self.mes = mes
        self.anio = anio

    @staticmethod
    def es_bisiesto(anio):
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    @staticmethod
    def dias_en_mes(mes, anio):
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mes in [4, 6, 9, 11]:
            return 30
        elif mes == 2:
            return 29 if Fecha.es_bisiesto(anio) else 28
        else:
            return 0

    def get_dia(self):
        return self.dia

    def get_mes(self):
        return self.mes

    def get_anio(self):
        return self.anio

    def set_dia(self, dia):
        if not self.es_fecha_valida(dia, self.mes, self.anio):
            raise ValueError("Día inválido")
        self.dia = dia

    def set_mes(self, mes):
        if not self.es_fecha_valida(self.dia, mes, self.anio):
            raise ValueError("Mes inválido")
        self.mes = mes

    def set_anio(self, anio):
        if not self.es_fecha_valida(self.dia, self.mes, anio):
            raise ValueError("Año inválido")
        self.anio = anio

    def mostrar(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

    @staticmethod
    def es_fecha_valida(dia, mes, anio):
        if anio < 1 or mes < 1 or mes > 12:
            return False
        return 1 <= dia <= Fecha.dias_en_mes(mes, anio)

    @classmethod
    def crear_desde_cadena(cls, fecha_str):
        try:
            fecha_str = fecha_str.replace("/", "-")  # Replace '/' with '-'
            partes = fecha_str.split('-')
            if len(partes) != 3:
                raise ValueError("Formato de fecha inválido")
            dia, mes, anio = map(int, partes)
            if not cls.es_fecha_valida(dia, mes, anio):
                raise ValueError("Fecha inválida")
            return cls(dia, mes, anio)
        except Exception as e:
            raise ValueError(f"Formato o fecha inválida: {fecha_str}. Error: {e}")
