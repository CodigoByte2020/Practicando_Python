#Comentario de una línea
'''Comentario de varias lineas
en Python'''

a=2
b=3
c="Gianmarco Contreras Pumamango"

print (a+b)
print (a); print(c)
print("Gianmarco Contreras Pumamango")

for i in range(5):
    print(i)

nombre="Gianmarco \
Contreras"
print(nombre)
print("Jose \
Contreras")

print(7**2)
print(10//3)
print(9%2)

print(type(nombre))

if (4>3):
    print("4 es mayor que 3")
else:
    print("4 NO es mayor que 3")


#Funciones
def message():
    print("Jose")
    print("Luis")
    print("Rodríguez")

message()
message()
print("Ejecutando código fuera de función")
message()

#Funciones con parámetros
def devuelve_suma(n1, n2):
    suma = n1 + n2
    return suma


print(devuelve_suma(7, 5))
ValorSuma = devuelve_suma(4, 10)
print(ValorSuma)

#Listas
mi_lista = ["Gian", True, 25, 150.50]
print(mi_lista[1:3])  # El primer valor incluye el index y el segundo valor excluye el index
print(mi_lista[:])  # Imprimimos todos los elementos de la lista
print(mi_lista[1:])  # Cuando falta un valor lo toma por defecto el primero o el último
print(mi_lista[-2])  # Cuando el valor es negativo python comienza a contar desde el valor final
print(mi_lista[1])
mi_lista.extend([10, False])  #Extiende una lista
mi_lista.remove(False) #Elimina un elemento en específico
mi_lista.append(555) #Agrega un elemento al final
mi_lista.insert(1, 2200) #Inserta un elemento en un index en específico
mi_lista.pop() #Elimina el ultimo elemento de la lista
print(mi_lista[:])

print("Mario" in mi_lista) #Verifica si el elemento se encuentra en la lista (True o False)
mi_lista2 = [1, 2, 3, 5, 10]
print(mi_lista + mi_lista2) #Concatena listas
print(mi_lista2 * 4) #Repetimos lista

print()

#tuplas

mi_tupla1 = 10, "Marcos", 25.3  # Empaquetado de tuplas
print("Empaquetado de tupla:", mi_tupla1)
print(mi_tupla1[1]) #Se indica el index del elemento que queremos imprimir de la tupla
mi_tupla2 = (20, "Jorge", 140)
print(mi_tupla2[2])
edad, nombre, sueldo = mi_tupla2 #Desempaquetado de tuplas
#mi_tupla2.append("Jorge") Una tupla no se puede modificar
print(mi_tupla2)
print("Tupla desempaquetada en variables", edad, ",", nombre, ',', sueldo)
print("Miguel" in mi_tupla2)
print(mi_tupla2.count(20))
print(len(mi_tupla2))
TuplaUnitaria = (200,)
print("Cantidad de elementos de la tupla unitaria", len(TuplaUnitaria))
print()

print(mi_tupla2)
milista3 = list(mi_tupla2)
print("Tupla cassteada a lista: ", milista3)

print()

print(mi_lista2)
mitupla3 = tuple(mi_lista2)
print("Lista cassteada a tupla", mitupla3)
#Listas entre corchetes [] y las tuplas entre paréntesis ()

print("")

#DICCIONARIOS clave:valor
mi_diccionario = {"peru": "lima", "venezuela": "caracas", "bolivia": "la paz", "argentina": "buenos aires"}
print(mi_diccionario)
mi_diccionario["suecia"] = "oslo" #Modo de agregar un elemento al diccionario
print(mi_diccionario)
mi_diccionario["suecia"] = "estocolmo" #Modo de modificar un elemento al diccionario
print(mi_diccionario)
print(mi_diccionario.keys()) #Obtemos las claves
print(mi_diccionario.values())#Obtenemos los valores
print(len(mi_diccionario))#Longitud del diccionario
del mi_diccionario["venezuela"]
print(mi_diccionario)
print()

lista5 = [1, 2, 3, 4]
mi_diccionario2 = {lista5[0]: "Jorge", lista5[1]: "Janeth", lista5[2]: "Anthony", lista5[3]: "Danna"}
print("Traemos las claves de un diccionario atraves de una lista: ", mi_diccionario2.keys())

tupla5 = (1, 2, 3, 4)
mi_diccionario3 = {tupla5[0]: "Jorge", tupla5[1]: "Janeth", tupla5[2]: "Anthony", tupla5[3]: "Danna"}
print("Traemos las claves de un diccionario atraves de una tupla: ", mi_diccionario3.keys())

#Podemos utilizar una lista o tupla para acceder a las claves o valores de un diccionario

tupla7 = (1, 2, 3, 4)
mi_diccionario4 = {"Jorge": tupla7[0], "Janeth": tupla7[1], "Anthony": tupla7[2], "Danna": tupla7[3]}
print("Traemos los valores de un diccionario atraves de una tupla: ", mi_diccionario4.values())

lista7 = [1, 2, 3, 4]
mi_diccionario5 = {"Jorge": lista7[0], "Janeth": lista7[1], "Anthony": lista7[2], "Danna": lista7[3]}
print("Traemos los valores de un diccionario atraves de una lista: ", mi_diccionario5.values())

print()

diccionario8 = {"nombre": "Gianmarco", "edad": 25, 3: [70493428, "DNI", "XXX"]}
print(diccionario8)
diccionario8 = {"nombre": "Gianmarco", "edad": 25, 3: (70493428, "DNI", "ZZZ")}
print(diccionario8[3])
#Un diccionario que contiene otro diccionario y que este a su vez contiene una lista
diccionario10 = {"nombre": "Gian", "edad": 25, "estudios": {"annios": [2000, 2010, 2014]}}
print(diccionario10)
#Un diccionario que contiene otro diccionario y que este a su vez contiene una tupla
diccionario10 = {"nombre": "Gian", "edad": 25, "estudios": {"annios": (2000, 2010, 2014)}}
print(diccionario10)
print(diccionario10.keys())
print(diccionario10.values())
print(len(diccionario10))
