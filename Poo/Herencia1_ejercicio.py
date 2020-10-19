class Vehiculo:

    propiedad1 = 1
    propiedad2 = 2

    def __init__(self, marco, precio):
        self.marco = marco
        self.precio = precio

    def informacion(self):
        return "La bicicleta tiene marco de " + self.marco + " y un precio de " + str(self.precio) + " soles."

class VehiculoElectrico:

    propiedad3 = 3

    def __init__(self, autonomia, cargador, modelo):
        self.autonomia = autonomia
        self.cargador = cargador
        self.modelo = modelo

    def getAutonomia(self):
        return self.autonomia

    def getCargador(self):
        print(self.cargador)


class Bicicleta(VehiculoElectrico, Vehiculo):
    pass

mi_bici = Bicicleta("aluminio", 1200, "deportivo")

#Atributos heredados de la clase Vehiculo
#print(mi_bici.informacion())
#print(mi_bici.autonomia) --- Propiedad no heredada, asi nos ayude el autocompletado (llamando al otro contructor)
print(mi_bici.propiedad1)
#print(mi_bici.marco)

#Atributos heredados de la clase VehiculoElectrico
print(mi_bici.propiedad3)
print(mi_bici.autonomia)
print(mi_bici.getAutonomia())
mi_bici.getCargador()

