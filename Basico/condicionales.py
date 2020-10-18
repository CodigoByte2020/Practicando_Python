# ESTRUCTURAS DE FLUJO

print("Programa para determinar si una persona es mayor de edad: ")
edad = int(input("Ingrese su edad: ")) #Todoo lo que se ingresa por input es texto

def calcular_edad(edad):
    mensaje = ""
    #if edad >= 0 and edad <= 17: forma redundante
    if 0 <= edad <= 17:
        mensaje = "Usted es menor de edad"
    elif 18 <= edad <=100: #En python usar and, or, not
        mensaje = "Usted es mayor de edad"
    else:
        mensaje = "Edad incorrecta"
    return mensaje

print(calcular_edad(edad))
print()

sueldo_gerente = int(input("Ingrese el sueldo del gerente: "))
print("El sueldo del gerente es: " + str(sueldo_gerente))

sueldo_administrador = int(input("Ingrese el sueldo del administrador: "))
print("El sueldo del administrador es: " + str(sueldo_administrador))

sueldo_empleado = int(input("Ingrese el sueldo del empleado: "))
print("El sueldo del empleado es: " + str(sueldo_empleado))

# Una condición con concatenación de operadores de comparación se lee de izquierda a derecha
if sueldo_empleado < sueldo_administrador < sueldo_gerente:
    print("Los sueldos son correctos")
else:
    print('Los sueldos son incorrectos')

#and or
print("Software para determinar si un alumno accede a una Beca")
salario = int(input("¿ Cuanto es tu salario ? "))
promedio = int(input("¿ Cuanto es tu promedio ? "))
sexo = input("¿ Eres hombre o mujer ? ")

if (salario < 2000 and promedio >= 18) and (sexo == "hombre" or sexo == "mujer"):
    print("SI accedes a la beca")
else:
    print("NO accedes a la beca")

#in
print("Software para determinar la validez de una asignatura")
asignatura = input("Elige una asignatura: Matemáticas, POO, Lógica: ").lower() #Convertimos la cadena a minúsculas
#asignatura = input("Elige una asignatura: Matemáticas, POO, Lógica: ").upper() #Convertimos la cadena a MAYÚSCULAS

if asignatura in ("matemáticas", "poo", "lógica"):
   print("Asignatura correcta")
else:
    print("Asignatura incorrecta")


