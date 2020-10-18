numero = int(input('Ingrese un número: '))
factorial = 0

def calcular_factorial(numero):
    factorial = numero
    if numero > 0:
        while numero >= 2:
            numero -= 1
            factorial *= numero
    elif numero == 0:
        factorial = 1
    else:
        raise ValueError("El número no puede ser menor que 0")
    return factorial

try:
    print('El factorial de ' + str(numero) + ' es: ' + str(calcular_factorial(numero)))
except ValueError as ExcLanzada:
    print(ExcLanzada)

print("El programa continúa con su ejecución normal")
print("Más líneas de código")
print("Más líneas de código")
print("Más líneas de código")
