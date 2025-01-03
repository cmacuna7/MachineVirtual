# *******************************************************************************************************
#            UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE                                                  
# Proposito:                      Nodo                                                                
# Autor:                          Marcelo Acuña                   
# Fecha de creacion:              17/12/2024                                                          
# Fecha de modificacion:          30/12/2024                                                          
# Materia:                        Estructura de datos                                                 
# NRC :                           1992                                                                
# *******************************************************************************************************

class Nodo:
    def __init__(self, persona):
        self.persona = persona
        self.siguiente = None
        self.anterior = None
