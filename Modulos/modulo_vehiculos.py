class Vehiculo:

    vagina = 20 #Se heredan las propiedades de la clase

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):#Se heredan los métodos de la clase
        self.en_marcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: " + self.marca + "\nModelo: " + self.modelo + "\nEn marcha: " + str(self.en_marcha)
              + "\nAcelerando: " + str(self.acelera) + "\nFrenando: " + str(self.frena))


class Moto(Vehiculo): #La clase Moto hereda de la clase Vehiculo sus atributos, constructor y métodos

    '''Variable hcaballito pertenece a cada objeto de la clase Moto, lo declaramos aca, porque si no se llama al método
    caballito y no se declare dicha variable dará error en el método estado'''
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Haciendo el caballito"

    def estado(self):
        print("Marca: " + self.marca + "\nModelo: " + self.modelo + "\nEn marcha: " + str(self.en_marcha)
              + "\nAcelerando: " + str(self.acelera) + "\nFrenando: " + str(self.frena) + "\n" + self.hcaballito)


mi_moto = Moto("Toyota", "Sport") #Se pasan los argumentos que necesita el constructor de la clase padre (Vehiculo)
mi_moto.caballito()
mi_moto.estado()


class Furgoneta(Vehiculo):

    def carga(self, cargar):
        self.cargado = cargar

        if self.cargado:
            return "La furgoneta esta cargada"

        else:
            return "La furgoneta esta descargada"


print("<------------------------ Furgoneta ---------------------------->")
mi_furgoneta = Furgoneta("Lebrinz", "pulpex")
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print(mi_furgoneta.carga(True))


class VElectricos(Vehiculo):

    trola = "pinga" #Se heredan las propiedades de la clase

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self): #Se heredan los métodos de la clase
        self.cargando = True
