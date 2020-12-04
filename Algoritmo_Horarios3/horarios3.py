'''oficina = [['D','X','N','N','N','N','N','N','X','D','D','D','D','D','D','X','N','N','N','N','N','N','X','D','D','D','D','D','D','X'],
           ['N','N','X','D','D','D','D','D','D','X','N','N','N','N','N','N','X','D','D','D','D','D','D','X','N','N','N','N','N','N']]

almacen = [['D','D','D','X','N','N','N','N','N','N','X','D','D','D','D','D','D','X','N','N','N','N','N','N','X','D','D','D','D','D'],
           ['N','N','N','N','X','D','D','D','D','D','D','X','N','N','N','N','N','N','X','D','D','D','D','D','D','X','N','N','N','N'],
           ['N','N','N','X','N','N','N','N','N','N','X','N','N','N','N','N','N','X','N','N','N','N','N','N','X','N','N','N','N','N']]

peaje =   [['D','D','D','D','D','X','N','N','N','N','N','N','X','D','D','D','D','D','D','X','N','N','N','N','N','N','X','D','D','D'],
           ['N','N','N','N','N','N','X','D','D','D','D','D','D','X','N','N','N','N','N','N','X','D','D','D','D','D','D','X','N','N'],
           ['N','N','N','N','N','X','N','N','N','N','N','N','X','N','N','N','N','N','N','X','N','N','N','N','N','N','X','N','N','N']]

descanse = [['X','D','D','D','D','D','D','X','N','N','N','N','N','N','X','D','D','D','D','D','D','X','N','N','N','N','N','N','X','D']]
reten =    [['X','X','X','N','X','N','X','X','X','X','N','X','N','X','X','X','X','N','X','N','X','X','X','X','N','X','N','X','X','X']]'''

oficina = [['D', 'X', 'N', 'N', 'N', 'N', 'N'],
           ['N', 'N', 'X', 'D', 'D', 'D', 'D']]

almacen = [['D', 'D', 'D', 'X', 'N', 'N', 'N'],
           ['N', 'N', 'N', 'N', 'X', 'D', 'D'],
           ['N', 'N', 'N', 'X', 'N', 'N', 'N']]

peaje =   [['D', 'D', 'D', 'D', 'D', 'X', 'N'],
           ['N', 'N', 'N', 'N', 'N', 'N', 'X'],
           ['N', 'N', 'N', 'N', 'N', 'X', 'N']]

descanse =[['X', 'D', 'D', 'D', 'D', 'D', 'D']]
reten =   [['X', 'X', 'X', 'N', 'X', 'N', 'X']]

'''for ii in matriz:
    for j in ii:
        for i in j:
            print('[' + i + ']', end=' ')
        print()
    print()'''
# k = columna de matriz
# j = fila de listas internas
# i = columna de listas internas
matriz = [oficina, almacen, peaje, descanse, reten]
Dxcolumna = 0
Nxcolumna = 0
#Xxcolumna = 0

#unidad_fallada = 0
descansos_fila = 0

descansos_columna = 0
#cantidad_Ds = 0
#cantidad_Ns = 0
#cantidad_DNs = 0
# = 0

'''for i in range(7):
    for k in range(len(matriz)):
        for j in range(len(matriz[k])):
            if 'D' in matriz[k][j][i]:
                Dxcolumna += 1
            elif 'N' in matriz[k][j][i]:
                Nxcolumna += 1
            elif 'X' in matriz[k][j][i]:
                Xxcolumna += 1
        j = 0'''

# posiciones_descanso = []
columnas_descanso = []

# Validamos que cada trabajador tenga un descanso, excepto el descansero 2 - Validación por fila
for k in range(len(matriz)):
    for j in range(len(matriz[k])):
        for i in range(len(matriz[k][j])):
            if 'X' in matriz[k][j][i]:
                '''posicion_descanso = []
                posicion_descanso.append(k)
                posicion_descanso.append(j)
                posicion_descanso.append(i)
                posiciones_descanso.append(posicion_descanso)'''
                if k < len(matriz) - 1:
                    if descansos_fila == 0:
                        columnas_descanso.append(i)
                elif k == len(matriz) - 1:
                    columnas_descanso.append(i)
                descansos_fila += 1

        if k < len(matriz) - 1:
            if descansos_fila != 1:
                print('ERROR en la cantidad de descansos por trabajador.')
                print('Fila [' + str(j) + ']: ' + str(descansos_fila) + ' descansos.')
            descansos_fila = 0

        elif k == len(matriz) - 1:
            if descansos_fila != 5:
                print('ERROR en la cantidad de descansos del descansero 2.')
                print('Fila [' + str(j) + ']: ' + str(descansos_fila) + ' descansos.')


# Validamos la cantidad de Ds y Ns en cada día - Validación por columna
for i in range(7):
    for k in range(len(matriz)):
        for j in range(len(matriz[k])):
            if 'D' in matriz[k][j][i]:
                Dxcolumna += 1
            elif 'N' in matriz[k][j][i]:
                Nxcolumna += 1
    if Dxcolumna != 3 or Nxcolumna != 5:
        print('ERROR en la repartición de turnos por día.')
        print('Columna [' + str(i) + ']:')
        print('D = ' + str(Dxcolumna))
        print('N = ' + str(Nxcolumna))
    Dxcolumna = 0
    Nxcolumna = 0


rol_servicio = [
    {'U1': oficina},
    {'U2': almacen},
    {'U3': peaje},
    {'U4': descanse},
    {'U5': reten}
]

unidad_validacion = \
    {'U1': [1, 1],
     'U2': [1, 2],
     'U3': [1, 2],
     'U4': [1, 0],
     'U5': [0, 1]}

i = 0
#index_temp = 0

#Validamos la distribución de Ds y Ns en cada unidad - Validación por columna de unidad
for unidad in rol_servicio:
    for key, value in unidad.items():
        validacion = unidad_validacion[key]
        # temp = []
        for i in range(len(value[0])):
            d = n = 0
            for j in range(len(value)):
                if unidad[key][j][i] == 'D':
                    d += 1
                elif unidad[key][j][i] == 'N':
                    n += 1
            if d > unidad_validacion[key][0]:
                print('ERROR, exceso de día(s) en la unidad: ' + key + '. ' + str(d) + ' días')
            elif n > unidad_validacion[key][1]:
                print('ERROR, exceso de noche(s) en la unidad: ' + key + '. ' + str(n) + ' noches')
