class Main:

    def __init__(self):
        self.semana = 7
        self.descansos_trabajador_semana = 0
        self.cantidad_unidades = 3

                        # 1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30
        self.oficina = [['D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X'],
                        ['N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N']]

        self.almacen = [['D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D'],
                        ['N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N'],
                        ['N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N']]

        self.peaje =   [['D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D'],
                        ['N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N'],
                        ['N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'N', 'N', 'N']]

        self.descanseros=[['X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'X', 'N', 'N', 'N', 'N', 'N', 'N', 'X', 'D'],
                          ['X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X', 'X', 'N', 'X', 'N', 'X', 'X', 'X']]

        self.trabajadores_unidad = {
                'U1': 2,
                'U2': 3,
                'U3': 3,
                'descanseros': 2
        }
        
        self.rol_servicio = [
            {'U1': self.oficina},
            {'U2': self.almacen},
            {'U3': self.peaje},
            {'descanseros': self.descanseros}
        ]

        self.turno_dia = 3
        self.turno_noche = 5

        self.unidad_validacion = {
            'U1': [1, 1],  # diurno - nocturno
            'U2': [1, 2],
            'U3': [1, 2]
        }

        self.apoyos = []

    def hallar_apoyos(self):
        for unidad in self.rol_servicio:
            for key, value in unidad.items():
                for j in range(len(unidad[key])):
                    temp_apoyo = {}
                    D = N = 0
                    for i in range(len(value[j])):
                        if unidad[key][j][i] == 'D':
                            D += 1
                        elif unidad[key][j][i] == 'N':
                            N += 1
                    if D > 14 or N > 14:
                        temp_apoyo[key] = j
                        self.apoyos.append(temp_apoyo)

    # Validamos que cada trabajador tenga sus horarios adecuados - Validación por fila
    def validacion_descansos_fila(self):
        for unidad in self.rol_servicio:
            for key1, value1 in unidad.items():
                for j in range(len(unidad[key1])):
                    turno = ''
                    for i in range(len(value1[j])):
                        if i == 0:
                            if unidad[key1][j][i] == 'D' or unidad[key1][j][i] == 'N':
                                turno = unidad[key1][j][i]
                            elif unidad[key1][j][i] == 'X':
                                turno = unidad[key1][j][i + 1]
                        else:
                            for apoyo in self.apoyos:
                                for key2, value2 in apoyo.items():
                                    if key1 == key2 and value1 == value2:
                                        break
                                        pass
                                    else:
                                        if unidad[key1][j][i] == 'X':
                                            if unidad[key1][j][i - 1] == 'D':
                                                turno = 'N'
                                            if unidad[key1][j][i - 1] == 'N':
                                                turno = 'D'
                                        elif unidad[key1][j][i] == turno:
                                            continue
                                        elif unidad[key1][j][i] != turno:
                                            print('ERROR en los horarios del trabajador #' + str(j + 1) + ' que pertenece a la unidad ' + key1)

    '''def validacion_descanso_fila(self):
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
                                    print('El trabajador ' + str(j + 1) + ' tiene ' + str(self.descansos_trabajador_semana) + ' descanso(s).')'''

    # Validamos la cantidad de Ds y Ns en cada día - Validación por columna
    def validacion_turnos_columna(self):
        d_columna = n_columna = 0
        for i in range(len(self.rol_servicio[0]['U1'][0])):
            for unidad in self.rol_servicio:
                for key, value in unidad.items():
                    for j in range(len(unidad[key])):
                        if unidad[key][j][i] == 'D':
                            d_columna += 1
                        elif unidad[key][j][i] == 'N':
                            n_columna += 1
            if d_columna != self.turno_dia:
                print('ERROR en la repartición de turnos por día, columna #' + str(i + 1) + ':')
                print('D = ' + str(d_columna))
            elif n_columna != self.turno_noche:
                print('ERROR en la repartición de turnos por día, columna #' + str(i + 1) + ':')
                print('N = ' + str(n_columna))
            d_columna = n_columna = 0


    #Validamos la distribución de Ds y Ns en cada unidad - Validación por turnos de unidad
    def validacion_turnos_unidad(self):
        i = 0
        for unidad in self.rol_servicio:
            for key, value in unidad.items():
                if key != 'descanseros':
                    validacion = self.unidad_validacion[key]
                else:
                    continue
                for i in range(len(value[0])):
                    d = n = 0
                    for j in range(len(value)):
                        if unidad[key][j][i] == 'D':
                            d += 1
                        elif unidad[key][j][i] == 'N':
                            n += 1
                    if d != self.unidad_validacion[key][0]:
                        print('ERROR, cantidad de día(s) en la unidad: ' + key + '. ' + str(d) + ' días')
                    elif n != self.unidad_validacion[key][1]:
                        print('ERROR, cantidad de noche(s) en la unidad: ' + key + '. ' + str(n) + ' noches')


if __name__ == '__main__':
    main = Main()
    main.hallar_apoyos()
    main.validacion_descansos_fila()
    main.validacion_turnos_columna()
    main.validacion_turnos_unidad()
