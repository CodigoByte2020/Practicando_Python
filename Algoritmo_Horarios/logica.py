import random

class Logica:
    __dias_trabajo = 0
    __dias_descanso = 0
    __cantidad_puestos = 0
    __lista_horarios = [[], []]
    bandera_trabajador = False
    bandera_dia = False

    def __init__(self, dias_trabajo, dias_descanso, cantidad_puestos):
        self.__dias_trabajo = dias_trabajo
        self.__dias_descanso = dias_descanso
        self.__cantidad_puestos = cantidad_puestos
        self.__lista_horarios = [[cantidad_puestos], [dias_trabajo]]

    def getAleatorios(self):
        numero_generado = 0
        for j in range(self.__cantidad_puestos):
            for i in range(self.__dias_trabajo):
                numero_generado = random.radint(0, 1)

        return self.__lista_horarios
