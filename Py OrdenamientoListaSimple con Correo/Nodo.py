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
        """
        Constructor de un nodo de la lista simplemente enlazada.
        :param persona: Objeto de tipo Persona.
        """
        self.persona = persona  # Almacena un objeto Persona
        self.siguiente = None   # Puntero al siguiente nodo, inicialmente None
