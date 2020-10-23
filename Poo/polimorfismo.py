class Coche:

    def desplazamiento(self):
        print("Me desplazo en 4 ruedas")

class Moto:

    hola = 10

    def __init__(self):
        self.chau = 200

    def desplazamiento(self):
        print("Me desplazo en 2 ruedas")

class Camion:

    def desplazamiento(self):
        print("Me desplazo en 6 ruedas")


#Se recibe como parámetro el objeto mi_moto y se almacena en el objeto vehiculo
def desplazamiento_general(vehiculo): #Polimorfismo en acción, el objeto vehiculo toma la forma del objeto recibido
    vehiculo.desplazamiento()

#mi_moto = Moto - Aca estoy guardando la clase Moto en mi_moto
mi_moto = Moto()
desplazamiento_general(mi_moto)
mi_moto = Camion() #El objeto mi_moto es mutable y cambia de forma a tipo Camion
desplazamiento_general(mi_moto)

mi_coche = Coche()
desplazamiento_general(mi_coche)
