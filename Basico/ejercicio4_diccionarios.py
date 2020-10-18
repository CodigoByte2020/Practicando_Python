'''Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato'''

dictionary = {}
decision = "si"
total = 0

while decision == "si":
    dato = input("Ingrese un artículo y su respectivo precio: ") #articulo:precio
    clave, valor = dato.split(":")
    dictionary[clave] = valor
    decision = input("Desea seguir ingresando datos: (si/no) ")

for i in dictionary:
    print(i + "     " + dictionary[i])
    total += int(dictionary[i])

print("Total     " + str(total))
#---------------------------------- OK ----------------------------------------------
