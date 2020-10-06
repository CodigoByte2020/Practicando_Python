#PALÍNDROMAS CON STRING:

frase = input("Ingrese una palabra o frase: ").lower().replace(" ", "")
puntero1 = 0
puntero2 = len(frase) - 1

while puntero1 < puntero2:

    #print(frase[puntero1] + " - " + frase[puntero2])

    if frase[puntero1] == frase[puntero2]:
        puntero1 += 1
        puntero2 -= 1
    else:
        print("La palabra o frase NO es palíndroma")
        break

else:
    print("La palabra o frase SI es palíndroma")
