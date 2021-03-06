# tupla = tuple([1, False, 'Gianmarco', 'Contreras'])
# print(tupla)
#
# lista = list(tupla)
# print(lista)
#
# lista_decimal = list(range(10))
# print(lista_decimal)
#
# # lista_decimal2 = lista_decimal --- Apuntamos al mismo objeto con otra variable
# lista_decimal2 = list(lista_decimal) # Copiamos la lista_decimal en lista_decimal2
# print('#%s lista decimal2: %s' % (id(lista_decimal2), lista_decimal2))
# print('#%s lista decimal1: %s' % (id(lista_decimal), lista_decimal))
#
# # ---------------------------
# letras = list()
# letras.append('a')
# letras_copy = list(letras)
# letras_copy.append('b')
# print('#letras: %s' % letras)
# print('#letras_copy: %s' % letras_copy)

#------------------------------------------------------------------------------------------
listita = [5, 7, 9, 6, 23, 4, 45]

listita_copia = []
for i in range(len(listita) - 1, -1, -1):
    listita_copia = listita_copia + [listita[i]]
print(listita_copia)

listita_copia2 = []
for j in range(len(listita)):
    listita_copia2 = [listita[j]] + listita_copia2
print(listita_copia)

listita_copia3 = list([listita[i] for i in range(len(listita) - 1, -1, -1)])
print(listita_copia3)

listita_copia4 = listita[::-1]
print(listita_copia4)

listita_copia5 = []
for i in listita:
    listita_copia5 = [i] + listita_copia5
print(listita_copia5)

listita_copia6 = []
k = 0
for k in range(len(listita)):
    listita_copia6.append(listita[len(listita) - 1 - k])
print(listita_copia6)

cuenta_atras = list(range(10, -1, -1))
cuenta_adelante = cuenta_atras[:]
cuenta_adelante.reverse()
print(cuenta_adelante)

