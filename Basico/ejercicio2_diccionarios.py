#DICCIONARO VACIO PREGUNTON
informacion = {}
decisión = "Si"

while decisión == "Si":
    key = input("¿Que información deseas guardar? ")
    value = input(key + ": ")
    informacion[key] = value
    print(informacion)
    decisión = input("¿Desea ingresar mas información? (Si/No) ")

#***************************** OK ***********************************