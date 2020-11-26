from datetime import date, datetime
from calendar import monthrange, monthcalendar

class Logica:
    __matriz = [[], []]

    def __init__(self, matriz_mes):
        '''self.__dia = dia
        self.__mes = mes
        self.__annio = annio
        self.lista_turnos = lista_turnos
        self.lista_descansos = lista_descansos'''
        self.matriz_mes = matriz_mes

    def matriz_personal(self):
        for j in matriz_mes:
            for i in j:
                print(i, end=' ')
            print()



fecha = input('Ingrese la fecha que comenzará a trabajar el personal (dd/mm/yyyy): ')
fecha = datetime.strptime(fecha, '%d/%m/%Y') #Parseamos la fecha ingresada a string
dia = fecha.day
mes = fecha.month
annio = fecha.year

semana = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}
numero_dia_mes = date.isoweekday(date(annio, mes, dia))
nombre_dia_mes = semana[numero_dia_mes]

numero_puestos = int(input('Ingrese el numero de puestos que desea cubrir: '))
turnos = ['Diurno', 'Nocturno', 'Descanso']
lista_turnos = []
lista_descansos = []
descanso = False
i = 0

print('Turnos: ' + str(turnos[:]))

while not descanso:
    while i < numero_puestos:
        turno = input('Ingresa el turno, en que empezará el personal #' + str(i + 1) + ": ").capitalize()
        if turno == 'Descanso':
            if descanso:
                print('ERROR, ya se ha registrado un personal que inicia sus labores en descanso.')
                print('Por favor vuelva a intentarlo.')
            else:
                lista_turnos.append(turno)
                descanso = True
                i += 1
        else:
            lista_turnos.append(turno)
            i += 1
    if not descanso:
        print('Debe haber un personal que empieze su turno descansando.')
        lista_turnos = []
        i = 0

i = 0

while i < numero_puestos:
    if i != lista_turnos.index('Descanso'):
        nombre_dia_descansar = input('Ingresa el nombre del día que descansará el personal #'
                                     + str(i + 1) + ": ").capitalize()
        if nombre_dia_descansar != nombre_dia_mes:
            if i == 0:
                lista_descansos.append(nombre_dia_descansar)
                i += 1
            else:
                if nombre_dia_descansar not in lista_descansos:
                    lista_descansos.append(nombre_dia_descansar)
                    i += 1
                else:
                    print('ERROR, ya existe un personal que descansa ese día')
        else:
            print('ERROR, ya existe un personal que descansa ese día')
    else:
        lista_descansos.append(nombre_dia_mes)
        i += 1

matriz_mes = monthcalendar(annio, mes)
print(matriz_mes)
print(lista_turnos)
print(lista_descansos)

#Falta sumar los diurnos y nocturnos


def get_cantidad_dias_mes(annio, mes):
    return monthrange(annio, mes)

cantidad_dias_mes = get_cantidad_dias_mes(annio, mes)
print('La cantidad de dias del mes es: ' + str(cantidad_dias_mes[1]))


objeto = Logica(matriz_mes)
objeto.matriz_personal()
