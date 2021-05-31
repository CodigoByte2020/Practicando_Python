import random


class Objeto:

    def __init__(self):
        self.lista_general = list()
        self.numero_filas = int(input('Ingrese el número de filas que tendrá la lista: '))

    def ingreso_datos(self):
        j = i = 0
        while j < self.numero_filas:
            self.lista_interna = []
            while i < 10:
                numero = random.randint(0, 9)
                self.lista_interna.append(numero)
                i += 1
            i = 0
            self.lista_general.append(self.lista_interna)
            j += 1
        return self.lista_general

    def sumar_datos(self):
        self.lista_general.append([0] * 10)
        j = 0
        i = len(self.lista_general[0]) - 1
        while i >= 0:  # columnas
            suma = 0
            while j < self.numero_filas:  # filas
                suma += self.lista_general[j][i]
            suma += self.lista_general[j][i]


objeto = Objeto()
objeto.ingreso_datos()
objeto.sumar_datos()
        
