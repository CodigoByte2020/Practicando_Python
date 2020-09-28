lista = []
limite = input("Ingrese la cantidad de elementos que tendrá la lista: ")

def genera_numeros_pares(limite):
    numero_par = 2
    for i in range(5):
        lista.append(numero_par)
        numero_par += 2
        return lista

print(genera_numeros_pares(limite))

