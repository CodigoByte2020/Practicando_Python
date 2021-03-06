class Conejo:

    nombre = "Bunny"
    raza = "Cabeza de león"
    edad = 1

    def información(self): #self hace referencia al objeto perteneciente a la clase
        return "El conejo " + self.nombre + " es de raza " + self.raza + " y tiene " + str(self.edad) + " año."

    def cumpleAnnios(self):
        self.edad += 1

    def ajjsajasj(self):  # Para poder llamar a un metodo en la misma clase, se debe hacer dentro de otro método
        self.cumpleAnnios()
        self.información()

    def edadActual(self):
        if self.edad == 1:
            return "El conejo es joven"
        else:
            return "El conejo es viejo"

mi_conejo = Conejo()
print("conejo " + str(mi_conejo.edad))
print(mi_conejo.información())
mi_conejo.cumpleAnnios()
print(mi_conejo.edadActual())

