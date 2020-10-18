#IMPRESIÓN DE NUMEROS SUCESIVOS:

# número_imprimir = 1
# cantidad_filas = int(input("Por favor introduce un número entero: "))
#
# for i in range(cantidad_filas):
#     número_imprimir = i * 2 + 1
#     while número_imprimir >= 1:
#         print(str(número_imprimir), end=" ")
#         número_imprimir -= 2
#     print("")

# ------------------------------ OK -------------------------------------

#NÚMERO PRIMO:

número = int(input("Introduce un número: "))
residuo = 0

for i in range(2, número, 1):
    residuo = número % i
    if residuo == 0:
        print("El número no es primo")
        break
else:
    print("El número es primo")