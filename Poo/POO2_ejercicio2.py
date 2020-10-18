class Bicicleta:

    #MÉTODO CONSTRUCTOR
    def __init__(self):
        self.__marco = "aluminio"
        self.__llantas = 2
        self.__precio = 800
        self.__horquilla = False

    def setPrecio(self, horquilla):
        self.__horquilla = horquilla

        if self.__horquilla:
            self.__precio += 200

    def getInformacion(self):
        if self.__horquilla:
            return "La bicicleta es de " + self.__marco + ", tiene " + str(self.__llantas) + " llantas, una " + \
                    "horquilla y tiene un precio de " + str(self.__precio) + " soles"
        else:
            return "La bicicleta es de " + self.__marco + ", tiene " + str(self.__llantas) + " llantas, no tiene " + \
                   "horquilla y tiene un precio de " + str(self.__precio) + " soles"


bicicleta_rutera = Bicicleta()
bicicleta_rutera.setPrecio(False)
print(bicicleta_rutera.getInformacion())

print("<----------------- OBJETO 2 ----------------->")

bicicleta_montanniera = Bicicleta()
bicicleta_montanniera.setPrecio(True)
print(bicicleta_montanniera.getInformacion())
