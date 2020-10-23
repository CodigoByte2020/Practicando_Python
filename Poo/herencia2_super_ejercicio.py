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

    def __init__(self, nombre, apellidos, edad, precio, pose_favorita):
        super().__init__(nombre, apellidos, edad)
        self.precio = precio
        self.pose_favorita = pose_favorita

    def informacion(self):
        return super().informacion() + " Precio: " + str(self.precio) + " Pose favorita: " + self.pose_favorita

puta = Prostituta("Johary", "Herrera Bazán", 18, 25, "De perrito")
print(isinstance(puta, Mujer)) #Una prostituta siempre es mujer, principio de sustitución
print(puta.informacion())
#************************** OK ***************************************

