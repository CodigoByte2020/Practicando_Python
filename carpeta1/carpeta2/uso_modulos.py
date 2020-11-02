#Si dentro de un paquete no hay modulo alguno, no es necesario crear un archivo llamado init
#Se coloca la ruta absoluta del módulo

# from Calculos.basicos.operaciones_basicas import *
# sumar(10, 25)
#
# from Calculos.calculos_generales import *
# sumar(20, 14)

from Calculos2.operaciones_basicas.srmd import *  # Importamos todos lo que se encuentra en el módulo srmd
restar(14, 4)


from Calculos2.operaciones_avanzadas.potencia import potencia  # Solo importamos la funcion potencia del módulo potencia
potencia(4, 3)


from Calculos2.operaciones_basicas.srmd import multiplicar
multiplicar(3, 8)
