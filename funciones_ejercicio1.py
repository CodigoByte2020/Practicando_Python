'''Escribir una función que reciba un número entero positivo y devuelva su factorial.'''
numero = int(input('Ingrese un número: '))
factorial = 0

def calcular_factorial(numero):
    factorial = numero
    if numero:
        while numero >= 2:
            numero -= 1
            factorial *= numero
    else:
        factorial = 0
    return factorial

print('El factorial de ' + str(numero) + ' es: ' + str(calcular_factorial(numero)))
# verificar porque devuelve none