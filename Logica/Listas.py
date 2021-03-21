lista1 = [1, 2, 3, 4, 5] * len([0, 10, 24])
print(lista1)

jfejk = [[[], [], []], [[[[[[8], 2]]], 'ag']], [[], [], []]]
print(jfejk)
lista2 = [[11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

lista3 = []

for j in range(3):
    lista4 = []
    lista3.append(lista4)
    for i in range(5):
        lista4.append(21)

# print('[', end='')
# for j in lista3:
#     print('[', end='')
#     for i in j:
#         print('{}, '.format(i), end='')
#     print('')
# print(']')

lista5 = ['Gianmarco', 'Contreras', 'Pumamango']

for j in range(len(lista5)):
    for i in range(len(lista5[j])):
        print('{}'.format(lista5[j][i]), end=' ')
    print()



