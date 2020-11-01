'''import funciones_matematicas

funciones_matematicas.sumar(10, 5)
funciones_matematicas.restar(10, 5)
funciones_matematicas.multiplicar(10, 5)
funciones_matematicas.dividir(10, 5)'''

'''from funciones_matematicas import sumar

sumar(4, 2)
restar(4, 2) #función no importada'''

# Este módulo se busca en el mismo nivel del directorio actualImportamos todos los componenetes de ese módulo
from funciones_matematicas import *

sumar(3, 2)
restar(3, 2)
multiplicar(3, 2)
dividir(3, 2)
