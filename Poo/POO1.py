class Coche():

    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    peso = 500
    mi_arranque = False

    def arrancar(self): #self hace referencia al objeto perteneciente a la clase
        self.mi_arranque = True

    def estado(self):
        if self.mi_arranque:
            return "El coche esta en movimento"
        else:
            return "El coche esta detenido"

mi_coche = Coche()
mi_coche.arrancar()
print(mi_coche.estado())
