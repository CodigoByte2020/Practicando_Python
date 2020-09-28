import math


print("Programa para calcular la raiz cuadrada de un numero")
intentos = 2

while intentos >= 0: #Siempre intentar reducir la condición
    numero = int(input("Ingresa un número: "))
    if numero >= 0:
        #intentos = -1
        break #La instrucción break corta el ciclo
    else:
        print("No se puede calcular la raíz cuadrada de un número negativo")
        if intentos > 0:
            print("Te quedan " + str(intentos) + " intentos")
        else:
            print("Ya no le quedan intentos, el programa finalizará")
        intentos -= 1

if numero >= 0:
    print("La raíz cuadrada de " + str(numero) + " es: " + str(math.sqrt(numero)))

for i in "Gianmarco Contreras":
    if i == " ":
        continue #salta a la siguiente iteración del bucle
    print(i, end=" ")

while 1:
   pass

class MiClase:
  pass #Operación nula, cuando se ejecuta no sucede nada

validacion = 0
email = str(input("Introduce tu email: "))

for i in email:
    if i == "@":
        validacion = 1
        break
else:
    validacion = 2 #Solo se ejecutará cuando el ciclo for haya terminado sus iteraciones, este else pertenece al for

print(validacion)
