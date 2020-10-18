#Cantidad de vocales en una palabra

palabra = input("Ingresa un palabra: ")
vocales = ["a", "e", "i", "o", "u"]
cantidad_vocales = [0, 0, 0, 0, 0]

for i in palabra:
    for j in range(len(vocales)):
        if i == vocales[j]:
            cantidad_vocales[j] += 1
            break #Este break solo corta el ciclo mas pequeño

for i in range(len(vocales)):
    print(f"Vocal {vocales[i]} - cantidad: {cantidad_vocales[i]}")

#************************* OK ****************************************
