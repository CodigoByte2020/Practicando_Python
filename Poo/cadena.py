class Cadenas:

    '''nombre = input("Ingresa tu nombre: ")

    print(nombre.lower()) #Devuelve la cadena convertida a minúsculas
    print(nombre.upper()) #Devuelve la cadena a mayúsculas
    print(nombre.capitalize())#Devuelve la cadena con su primera letra a mayúsculas'''

    while True:
        edad = input("Ingresa tu edad: ")
        if edad.isdigit() == True:
            break

    if int(edad) >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

