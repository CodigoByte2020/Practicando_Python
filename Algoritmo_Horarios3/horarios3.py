class Main:

    def __init__(self):
        self.semana = 7
        self.descansos_trabajador_semana = 0
        self.cantidad_unidades = 3
        self.turno_dia = 3
        self.turno_noche = 5

                        # 1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30
        self.oficina = [['D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X'],
                        ['N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N']]

        self.almacen = [['D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D'],
                        ['N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N'],
                        ['N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N']]

        self.peaje =   [['D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D'],
                        ['N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N'],
                        ['N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N']]

        self.descansero=[['X','D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D']]

        self.reten =   [['X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X']]

        self.rol_servicio = [
            {'U1': self.oficina},
            {'U2': self.almacen},
            {'U3': self.peaje},
            {'descansero': self.descansero},
            {'reten': self.reten}
        ]

        self.unidad_validacion = \
            {'U1': [1, 1],  # diurno - nocturno
             'U2': [1, 2],
             'U3': [1, 2],
             'descansero': [1, 0],
             'reten': [0, 1]}



    # Validamos que cada trabajador tenga 1 descanso por semana (excepto el reten) - Validación por fila
    def validacion_descanso_fila(self):
        for unidad in self.rol_servicio:
            for key, value in unidad.items():
                for j in range(len(unidad[key])):
                    self.descansos_trabajador_semana = 0
                    for i in range(len(value[0])):
                        if unidad[key][j][i] == 'X':
                            self.descansos_trabajador_semana += 1
                        if i == self.semana - 1:
                            if key != 'reten':
                                if self.descansos_trabajador_semana != 1:
                                    print('ERROR en la cantidad de descansos por trabajador')
                                    print('Unidad: ' + key)
                                    print('El trabajador ' + str(j + 1) + ' tiene ' + str(self.descansos_trabajador_semana) + ' descanso(s).')

    # Validamos la cantidad de Ds y Ns en cada día - Validación por columna
    def validacion_turnos_columna(self):
        i = 0
        d_columna = n_columna = 0
        for i in range(len(self.rol_servicio[0]['U1'][0])):
            for unidad in self.rol_servicio:
                for key, value in unidad.items():
                    for j in range(len(unidad[key])):
                        if unidad[key][j][i] == 'D':
                            d_columna += 1
                        elif unidad[key][j][i] == 'N':
                            n_columna += 1
            if d_columna != self.turno_dia or n_columna != self.turno_noche:
                print('ERROR en la repartición de turnos por día.')
                print('Columna [' + str(i + 1) + ']:')
                print('D = ' + str(d_columna))
                print('N = ' + str(n_columna))
            d_columna = n_columna = 0

    #Validamos la distribución de Ds y Ns en cada unidad - Validación por turnos de unidad
    def validacion_turnos_unidad(self):
        i = 0
        for unidad in self.rol_servicio:
            for key, value in unidad.items():
                validacion = self.unidad_validacion[key]
                for i in range(len(value[0])):
                    d = n = 0
                    for j in range(len(value)):
                        if unidad[key][j][i] == 'D':
                            d += 1
                        elif unidad[key][j][i] == 'N':
                            n += 1
                    if key == 'descansero':
                        #Para el descansero aplicamos el intercambio de valores, como en el algoritmo de la burbúja
                        temp = 0
                        if i == self.semana or i == self.semana * 2 or i == self.semana * 3 or i == self.semana * 4:
                            temp = self.unidad_validacion[key][0]
                            self.unidad_validacion[key][0] = self.unidad_validacion[key][1]
                            self.unidad_validacion[key][1] = temp
                    if d > self.unidad_validacion[key][0]:
                        print('ERROR, exceso de día(s) en la unidad: ' + key + '. ' + str(d) + ' días')
                    elif n > self.unidad_validacion[key][1]:
                        print('ERROR, exceso de noche(s) en la unidad: ' + key + '. ' + str(n) + ' noches')


if __name__ == '__main__':
    main = Main()
    main.validacion_descanso_fila()
    main.validacion_turnos_columna()
    main.validacion_turnos_unidad()
