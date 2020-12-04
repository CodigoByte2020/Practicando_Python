class Main:

    def __init__(self):
        self.Dxcolumna = 0
        self.Nxcolumna = 0
        self.descansos_fila = 0

        self.oficina = [['D', 'X', 'N', 'N', 'N', 'N', 'N'],
                   ['N', 'N', 'X', 'D', 'D', 'D', 'D']]

        self.almacen = [['D', 'D', 'D', 'X', 'N', 'N', 'N'],
                   ['N', 'N', 'N', 'N', 'X', 'D', 'D'],
                   ['N', 'N', 'N', 'X', 'N', 'N', 'N']]

        self.peaje = [['D', 'D', 'D', 'D', 'D', 'X', 'N'],
                 ['N', 'N', 'N', 'N', 'N', 'N', 'X'],
                 ['N', 'N', 'N', 'N', 'N', 'X', 'N']]

        self.descansero = [['X', 'D', 'D', 'D', 'D', 'D', 'D']]

        self.reten = [['X', 'X', 'X', 'N', 'X', 'N', 'X']]

        self.__rol_servicio = [
            {'U1': self.oficina},
            {'U2': self.almacen},
            {'U3': self.peaje},
            {'U4': self.descansero},
            {'U5': self.reten}
        ]

        self.__unidad_validacion = \
            {'U1': [1, 1],
             'U2': [1, 2],
             'U3': [1, 2],
             'U4': [1, 0],
             'U5': [0, 1]}

    # Validamos que cada trabajador tenga un descanso, excepto el reten - Validación por fila
    def validacion_descanso_fila(self):
        for unidad in self.__rol_servicio:
            for key, value in unidad.items():
                for j in range(len(unidad[key])):
                    descansos_fila = 0
                    for i in range(len(value[0])):
                        if unidad[key][j][i] == 'X':
                            descansos_fila += 1
                    if key != 'U5':
                        if descansos_fila != 1:
                            print('ERROR en la cantidad de descansos por trabajador')
                            print('Fila [' + str(j) + ']: ' + str(descansos_fila) + ' descansos.')
                    else:
                        if descansos_fila != 5:
                            print('ERROR en la cantidad de descansos por trabajador')
                            print('Fila [' + str(j) + ']: ' + str(descansos_fila) + ' descansos.')

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

    #Validamos la distribución de Ds y Ns en cada unidad - Validación por columna de unidad
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
                    if d > self.__unidad_validacion[key][0]:
                        print('ERROR, exceso de día(s) en la unidad: ' + key + '. ' + str(d) + ' días')
                    elif n > self.__unidad_validacion[key][1]:
                        print('ERROR, exceso de noche(s) en la unidad: ' + key + '. ' + str(n) + ' noches')



if __name__ == '__main__':
    main = Main()
    main.validacion_descanso_fila()
    main.validacion_turnos_columna()
    main.validacion_turnos_unidad()


    