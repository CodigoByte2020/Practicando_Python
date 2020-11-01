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