class Bicicleta:

    #MÉTODO CONSTRUCTOR
    def __init__(self):
        self.__marco = "aluminio"
        self.__llantas = 2
        self.__precio = 800
        self.__horquilla = False

    def setHorquilla(self, horquilla):
        self.__horquilla = horquilla
        return self.__obtener_descuento()

    def __obtener_descuento(self):
        if self.__horquilla:
            self.__precio += 200

        if self.__precio == 1000:
            return "Su bicicleta tendrá un descuento del 25%: " + str(self.__precio * 0.25) + " soles"
        else:
            return "Su bicicleta no tiene descuento"

    def getInformacion(self):
        if self.__horquilla:
            return "La bicicleta es de " + self.__marco + ", tiene " + str(self.__llantas) + " llantas, una " + \
                    "horquilla y tiene un precio de " + str(self.__precio) + " soles"
        else:
            return "La bicicleta es de " + self.__marco + ", tiene " + str(self.__llantas) + " llantas, no tiene " + \
                   "horquilla y tiene un precio de " + str(self.__precio) + " soles"


bicicleta_rutera = Bicicleta()
bicicleta_rutera.setHorquilla(False)
print(bicicleta_rutera.getInformacion())

print("<----------------- OBJETO 2 ----------------->")

bicicleta_montanniera = Bicicleta()
bicicleta_montanniera.setHorquilla(True)
print(bicicleta_montanniera.getInformacion())
