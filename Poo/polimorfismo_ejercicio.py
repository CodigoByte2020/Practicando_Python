class Moto:
    def desplazamiento(self):
        print("Me desplazo en 2 ruedas")

class Coche:
    def desplazamiento(self):
        print("Me desplazo en 4 ruedas")

class Camion:
    def desplazamiento(self):
        print("Me desplazo en 6 ruedas")

mi_moto = Moto()
mi_coche = Coche()
mi_coche.peso = 200 #Agregamos la propiedad peso al objeto mi_coche
mi_camion = Camion()

lista_objetos = (mi_moto, mi_coche, mi_camion)

for i in lista_objetos: #Polimorfismo en acción
    i.desplazamiento()
