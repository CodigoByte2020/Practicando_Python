#PALÍNDROMAS CON LISTAS:

frase = input("Ingrese una palabra o frase: ").lower().replace(" ", "")
lista = []

for i in range(len(frase)):
    lista.append(frase[i])

puntero1 = 0
puntero2 = len(lista) - 1

while puntero1 < puntero2:

    print(frase[puntero1] + " - " + frase[puntero2])

    if lista[puntero1] == lista[puntero2]:
        puntero1 += 1
        puntero2 -= 1
    else:
        print("La palabra o frase NO es palíndroma")
        break

else:
    print("La palabra o frase SI es palíndroma")

