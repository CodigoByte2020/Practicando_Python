lista_original = [4, 10, 18, 7, 12, 5, 25, 30, 21]

lista1 = list(lista_original)
lista1.sort(reverse=True)  # Modifica la lista1 y devuelve None, se aplica sobre una lista
print(lista_original)
print(lista1)

lista2 = sorted(lista_original, reverse=True)  # Retorna una nueva lista ordenada, se aplica sobre un iterable
print(lista_original)
print(lista2)
