class Coche():

    # Cuando colocamos 2 guiones bajos delante del nombre de variable la estamos encapsulando, para que solo pueda ser accedida desde dentro de la clase
    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4
        self.__peso = 500
        self.__mi_arranque = False

    def arrancar(self, arrancamos): #self hace referencia al objeto perteneciente a la clase
        self.__mi_arranque = arrancamos

        if self.__mi_arranque:
            checkeo = self.__checkeo_interno() #Variable local,accesible sólo en este método

        if self.__mi_arranque and checkeo:
            return "El checkeo interno funciono correctamente y el coche esta en movimento"

        elif self.__mi_arranque and checkeo == False:
            return "Algo fallo en el checkeo interno y el coche no pudo arrancar"

        else:
            return "El coche esta detenido"

    def __checkeo_interno(self): #encampsulamos el método para que sólo sea accedido desde la clase
        print("Empezando checkeo interno")
        self.gasolina = "ok" #Variables globales, pertenecen al objeto
        self.agua = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.agua == "ok" and self.puertas == "cerradas":
            return True

        else:
            return False


    def informacion(self):
        return "El coche tiene un largo de " + str(self.__largo_chasis) + " metros, un ancho de " + str(self.__ancho_chasis) \
            + " metros, " + str(self.__ruedas) + " ruedas y un peso de " + str(self.__peso) + " kilos."


mi_coche = Coche() #Creamos un objeto de clase y lo instanciamos
print(mi_coche.arrancar(True))
print(mi_coche.informacion())

print("<------------------- Aqui creamos el segundo objeto ----------------------------->")

mi_coche2 = Coche()
print(mi_coche2.arrancar(False))
print(mi_coche2.informacion())
#mi_coche2.ruedas = 10 #Al hacer esto el objeto mi_coche2 crea una nueva variable ruedas con el valor de 10
#mi_coche2.__ruedas = 20 #Se crea una variable encapsulada que se llama __ruedas

