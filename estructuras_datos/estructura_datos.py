# listas
# ,
# [] + []
# -1

lista1 = [5, ]
print(lista1)

animales = ['perro', 'gato', 'conejo', 'pavo']
print("animales: " + str(animales))

animales_domesticos = animales[:-2]
print("animales domesticos: " + str(animales_domesticos))

animales += ['cebra', 'tigre']
print("animales: " + str(animales))
animales_mundiales = animales + animales_domesticos
print('animales mundi: ' + str(animales_mundiales))
print('animales m * 2: ' + str(animales_mundiales * 2))

total_animales = animales_mundiales * 2
total_animales[6:-8] = ['culebra']
total_animales[-2:] = ['oso']
print('total animales: ' + str(total_animales))
total_animales[2:-1] = []
print('total animales: ' + str(total_animales))
total_animales[:] = []
print('total animales: ' + str(total_animales))
