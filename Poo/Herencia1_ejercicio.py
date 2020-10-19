class Vehiculo:

    def __init__(self, marco, precio):
        self.marco = marco
        self.precio = precio

    def informacion(self):
        return "La bicicleta tiene marco de " + self.marco + " y un precio de " + str(self.precio) + " soles."


class Bicicleta(Vehiculo):
    pass

mi_bici = Bicicleta("aluminio", 1200)
print(mi_bici.informacion())
