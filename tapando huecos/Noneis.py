def IsNone():

    numero = None  # tipo None, único valor None
    num = None
    print("%s: %s" % (numero, id(numero)))
    print("%s: %s" % (num, id(num)))
    while numero is None or numero > 0:
        numero = int(input("Ingrese un número mayor de 0: "))
    else:
        print("Ingresaste el número 0.")

IsNone()

nada = None
cero = 0
cinco = 5  # Los tipo de datos entero, None, etc son inmutables
cinko = 5

print("%s: %s" % (nada, id(nada)))
print("%s: %s" % (cero, id(cero)))
print("%s: %s" % (cinco, id(cinco)))
print("%s: %s" % (cinko, id(cinko)))

lis = [0, 1, 2, 3]
print("%s: %s" % (lis, id(lis)))  # Las listas y las tuplas si cambian su identificador
lista = [0, 1, 2, 3]
print("%s: %s" % (lista, id(lista)))
print(lis is lista)

tup = (0, 1, 2, 3)
print("%s: %s" % (tup, id(tup)))
tupla = (0, 1, 2, 3)
print("%s: %s" % (tupla, id(tupla)))

numero_cinco = 5
print("%s: %s" % (numero_cinco, id(numero_cinco)))

# Programa que pida 5 números y que compruebe cuál es el mayor

lista = []
mayor = 0
index = 0
for numero in range(5):
    lista.append(int(input("Ingrese un número: ")))
    if lista[index] > mayor:
        mayor = lista[index]
    index += 1
print(lista)
print('El mayor número de la lista es: %s' % mayor)

mayor = None
for i in range(5):
    numero = int(input('Ingrese un número: '))
    if mayor is None or numero > mayor:
        mayor = numero
print('El número mayor es %s ' % mayor)

lista = []
for i in range(5):
    numero = int(input('Ingrese un número: '))
    lista.append(numero)
print('El número mayor es: %s' % max(lista))

lista = []
for i in range(3):
    lista.append(lista.append(input('Ingrese un número: ')) if i < 3 else None)

