# BUCLES
# el ciclo for se repite el número de veces, de la cantidad de elementos que contiene la lista
# en cada vuelta la i guarda el valor de cada elemento de la lista
j = 1
for i in ["gato", 20.5, 6, 8, "bunny"]:
    print("Elemento #" + str(j), ":", i, end="  ")
    j += 1

print()
# Validar el email, puede tener entre 0 y 2 puntos y sólo una arroba
arroba = 0
punto = 0
email = input("Introduce tu email: ")

for i in email:
    if i == "@":
        arroba += 1
    if i == ".":
        punto += 1

if arroba == 1 and 1 <= punto <= 3:
    print("Email CORRECTO")
else:
    print("Email INCORRECTO")

# Tipo de dato range, según mis deducciones parece que también es de tipo entero
for i in range(5):
    print("Posición: ")
    print("[" + str(i) + "]") #De esta forma podemos manejar mejor los espacios
    #print("[", i, "]")

# Función f para concatenar texto y números
edad = 25
sexo = "hombre"
print(f"Me llamo Gianmarco, tengo {edad} años y soy {sexo}")
print()

#range: inicio:incluye, fin:excluye, autoincremento
for i in range(2, 10, 2):
    print(i, end=" ")

print()

correo = input("Ingresa tu correo: ")
valido = False
for i in range(len(correo)):
    if correo[i] == "@":
        valido = True

if valido:
    print("Correo válido")
else:
    print("Correo inválido")

