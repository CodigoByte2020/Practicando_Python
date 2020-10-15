'''Escribir una función generadora que devuelva 3 numeros primos, pero el usuario decidirá cuantos de estos quiere visualizar: '''

def numeros_primos(cantidad):
    numero = 2
    cantidad = 0
    while cantidad < 5 and numero >= 2:
        if numero == 2:
            cantidad += 1
            yield numero
            numero += 1
        else:
            for i in range(2, numero, 1): #Para salir del for con range, es necesario la instrucción break, no se puede cambiando el valor del iterador a un rango por fuera
                if numero % i == 0:
                    numero += 1
                    break
            else:
                cantidad += 1
                yield numero
                numero += 1

objeto_generador_iterable = numeros_primos(3)

print(next(objeto_generador_iterable))
print('Aqui va muchas líneas de código')
print(next(objeto_generador_iterable))
print('Aqui va muchas líneas de código')
print(next(objeto_generador_iterable))
print('Aqui va muchas líneas de código')

# ---------------------------------------- OK --------------------------------------------------