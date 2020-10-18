'''Escribir una función que genere numeros pares y los almacene en una lista'''

# Ejercicio con una función normal
# lista = []
#
# def generaPares(limite):
#     numero = 1
#     while numero <= limite:
#         lista.append(numero * 2)
#         numero += 1
#     return lista
#
# generaPares(5)
#
# for i in range(3):
#     print(lista[i], end=' ')

def generaPares(limite):
    numero = 1
    while numero <= limite:
        yield numero * 2 #Con la instruccion yield almacenamos un valor en un objeto generador iterable por cada llamada a este método
        numero += 1

objeto_generador_iterable = generaPares(5) #???
print(objeto_generador_iterable)
print(generaPares(5))

#for i in objeto_generador_iterable:
#    print(i)

#Es lo mismo que hacer un for a objeto_generador_iterable
# for i in generaPares(5):
#     print(i)

print("Generador en estado de suspensión")
print(next(objeto_generador_iterable)) #El generador realiza su trabajo y extrae el siguiente elemento que se genera en la función generaPares
print("Generador en estado de suspensión")
print('Aqui va muchas líneas de código')
print(next(objeto_generador_iterable)) #El generador realiza su trabajo y extrae el siguiente elemento que se genera en la función generaPares
print('Generador en estado de suspensión')
print('Aqui va muchas líneas de código')
print(next(objeto_generador_iterable)) #El generador realiza su trabajo y extrae el siguiente elemento que se genera en la función generaPares
print('Generador en estado de suspensión')

print(objeto_generador_iterable)


