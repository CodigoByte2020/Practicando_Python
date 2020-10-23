class Mujer:

    carisma = True

    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def informacion(self):
        return "Nombre: " + self.nombre + " Apellidos: " + self.apellidos + " Edad: " + str(self.edad)


class Prostituta(Mujer):

    fantasias = True

    def __init__(self, nombre, apellidos, edad, precio):
        super().__init__(nombre, apellidos, edad)
        self.precio = precio

    def informacion(self):
        super().informacion() + " Precio: " + str(self.precio)


puta = Prostituta("Johary", "Herrera Bazán", 18, 25)


