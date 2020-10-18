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
            return "El coche esta en movimento"
        else:
            return "El coche esta detenido"

    def informacion(self):
        return "El coche tiene un largo de " + str(self.__largo_chasis) + " metros, un ancho de " + str(self.__ancho_chasis) \
            + " metros, " + str(self.__ruedas) + " ruedas y un peso de " + str(self.__peso) + " kilos."


mi_coche = Coche() #Creamos un objeto de clase y lo instanciamos
print(mi_coche.arrancar(True))
print(mi_coche.informacion())

print("<------------------- Aqui creamos el segundo objeto ----------------------------->")

mi_coche2 = Coche()
print(mi_coche2.arrancar(False))
mi_coche2.ruedas = 10 #Al hacer esto el objeto mi_coche2 crea una nueva variable ruedas con el valor de 10
mi_coche2.__ruedas = 20 #Se crea una variable encapsulada que se llama __ruedas
print(mi_coche2.informacion())
