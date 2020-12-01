import random

class Logica:
    __lista_horarios = [[], []]
    bandera_trabajador = False
    bandera_dia = False

    def __init__(self, dias_trabajo, dias_descanso, cantidad_puestos):
        self.__dias_trabajo = dias_trabajo
        self.__dias_descanso = dias_descanso
        self.__cantidad_puestos = cantidad_puestos

    def getAleatorios(self):
        numero_generado = 0
        for j in range(self.__cantidad_puestos):
            for i in range(self.__dias_trabajo):
                numero_generado = random.randint(0, 1)
                self.__lista_horarios[j][i] = 1200
                numero_generado = 10

        return self.__lista_horarios

print("***************************************************************")
print("* SOFTWARE PARA CALCULAR EL HORARIO ADECUADO EN UNA EMPRESA X *")
print("***************************************************************")

dias_trabajo = int (input("¿Cuántos días de trabajo tendrá cada trabajador? "))
dias_descanso = int (input("¿Cuántos días de descanso tendrá cada trabajador? "))
cantidad_puestos = int (input("¿Cuántos puesto desea cubrir? "))

mensajero = Logica(dias_trabajo, dias_descanso, cantidad_puestos)
mensajero.getAleatorios()
