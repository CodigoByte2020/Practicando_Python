'''Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas.
El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir.'''

#DICCIONARIO ESPAÑOL - INGLÉS
palabras = input("Ingrese palabras en español: ingles, separadas por comas: ")
lista_palabras = palabras.split()
diccionario = {}

for i in palabras.split(","): #Si no se indica nada en el split, sera un espacio el delimitador, sino será el valor indicado y ya no el espacio
    clave, valor = i.split(":") #Desempaquetamos la lista retornada en 2 variables
    diccionario[clave] = valor

frase_espanniol = input("Ingrese una frase en español: ")
for i in frase_espanniol.split():
    if i in diccionario:
        print(diccionario[i], end=" ")
    else:
        print(i, end=" ")

#****************************************** OK **********************************
