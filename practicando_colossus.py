'''lista = []
intentos = 0

while(intentos < 3):
    lista.append(input("Ingrese un número: "))
    intentos += 1

print(lista[:2])

diccionario = {2: 'giannarco', 4: 'contreras', 6: 'pumamango'}

print(diccionario.keys())
print(diccionario.values())'''

lista2 = []
contador = 0
intentos = int(input("¿Cuantos intentos desea tener? "))

while contador < intentos:
    lista2.append(int(input("Ingrese un número: ")))
    contador += 1

print()

for i in range(len(lista2)):
    print(lista2[i])
