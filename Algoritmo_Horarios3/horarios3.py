class Main:

    def __init__(self):
        self.__Dxcolumna = 0
        self.__Nxcolumna = 0
        self.__descansos_fila = 0

        self.__oficina = [['D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X'],
                          ['N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N']]

        self.__almacen = [['D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D'],
                          ['N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N'],
                          ['N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N']]

        self.__peaje =   [['D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D'],
                          ['N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N'],
                          ['N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N']]

        self.__descanse= [['X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D']]

        self.__reten =   [['X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X']]

        self.__rol_servicio = [
            {'U1': self.__oficina},
            {'U2': self.__almacen},
            {'U3': self.__peaje},
            {'U4': self.__descanse},
            {'U5': self.__reten}
        ]

        self.__unidad_validacion = \
            {'U1': [1, 1],  # diurno - nocturno
             'U2': [1, 2],
             'U3': [1, 2],
             'U4': [1, 0],
             'U5': [0, 1]}

    # Validamos que cada trabajador tenga 4 o 5 descansos, excepto el reten - Validación por fila
    def validacion_descanso_fila(self):
        for unidad in self.__rol_servicio:
            for key, value in unidad.items():
                for j in range(len(unidad[key])):
                    self.__descansos_fila = 0
                    for i in range(len(value[0])):
                        if unidad[key][j][i] == 'X':
                            self.__descansos_fila += 1
                    if key != 'U5':
                        if self.__descansos_fila != 4 and self.__descansos_fila != 5:
                            print('ERROR en la cantidad de descansos por trabajador')
                            print('Unidad: ' + key)
                            print('El trabajador ' + str(j + 1) + ' tiene ' + str(self.__descansos_fila) + ' descanso(s).')
                    else:
                        if self.__descansos_fila != 22:
                            print('ERROR en la cantidad de descansos por trabajador')
                            print('Unidad: ' + key)
                            print('El trabajador ' + str(j + 1) + ' tiene ' + str(self.__descansos_fila) + ' descanso(s).')

    # Validamos la cantidad de Ds y Ns en cada día - Validación por columna
    def validacion_turnos_columna(self):
        i = 0
        d_columna = n_columna = 0
        for i in range(len(self.__rol_servicio[0]['U1'][0][0])):
            for unidad in self.__rol_servicio:
                for key, value in unidad.items():
                    for j in range(len(unidad[key])):
                        if unidad[key][j][i] == 'D':
                            d_columna += 1
                        elif unidad[key][j][i] == 'N':
                            n_columna += 1
            if d_columna != 3 or n_columna != 5:
                print('ERROR en la repartición de turnos por día.')
                print('Columna [' + str(i) + ']:')
                print('D = ' + str(d_columna))
                print('N = ' + str(n_columna))
            d_columna = n_columna = 0

    #Validamos la distribución de Ds y Ns en cada unidad - Validación por turnos de unidad
    def validacion_turnos_unidad(self):
        i = 0
        for unidad in self.__rol_servicio:
            for key, value in unidad.items():
                validacion = self.__unidad_validacion[key]
                for i in range(len(value[0])):
                    d = n = 0
                    for j in range(len(value)):
                        if unidad[key][j][i] == 'D':
                            d += 1
                        elif unidad[key][j][i] == 'N':
                            n += 1
                    if key == 'U4':
                        #Para el descansero aplicamos la lógica del algoritmo de la burbuja
                        semana = 7
                        temp = 0
                        if i == semana or i == semana * 2 or i == semana * 3 or i == semana * 4:
                            temp = self.__unidad_validacion[key][0]
                            self.__unidad_validacion[key][0] = self.__unidad_validacion[key][1]
                            self.__unidad_validacion[key][1] = temp
                    if d > self.__unidad_validacion[key][0]:
                        print('ERROR, exceso de día(s) en la unidad: ' + key + '. ' + str(d) + ' días')
                    elif n > self.__unidad_validacion[key][1]:
                        print('ERROR, exceso de noche(s) en la unidad: ' + key + '. ' + str(n) + ' noches')


if __name__ == '__main__':
    main = Main()
    main.validacion_descanso_fila()
    main.validacion_turnos_columna()
    main.validacion_turnos_unidad()
