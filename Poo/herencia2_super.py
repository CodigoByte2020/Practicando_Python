class Persona:

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre: " + str(self.nombre) + "\nEdad: " + str(self.edad) + "\nLugar de residencia: "
              + str(self.lugar_residencia))

class Empleado(Persona):

    def __init__(self, nombre, edad, lugar_residencia, sueldo, antiguedad): #Sobreescribimos el constructor de la clase padre
        super().__init__(nombre, edad, lugar_residencia) #Llamamos al constructor de la clase padre
        self.sueldo = sueldo
        self.antiguedad = antiguedad

    def descripcion(self): #Sobreescribimos el método descripcion de la clase padre
        super().descripcion() #Llamamos al método descripcion de la clase padre
        print("Sueldo: " + str(self.sueldo) + "\nAntigüedad: " + str(self.antiguedad))

    # def descripcion(self): #Forma no muy elegante de solucionar el problema de sobreescribir métodos
        # print("Nombre: " + str(self.nombre) + " Edad: " + str(self.edad) + " Lugar de residencia: "
        #       + str(self.lugar_residencia) + " Sueldo: " + str(self.sueldo) + " Antigüedad: " + str(self.antiguedad))


empleado1 = Empleado("Gianmarco", 28, "Perú", 1200, 5)
#print(empleado1.nombre) #Ahora el objeto empleado1 posee la propiedad nombre
empleado1.descripcion()

# Un empleado siempre es una persona, una persona no siempre es un empleado --- PRINCIPIO DE SUSTITUCIÓN
# El objeto empleado1 es de tipo Empleado y Persona)
print(isinstance(empleado1, Empleado))
print(isinstance(empleado1, Persona))
print("-------------------------------- OK ------------------------------------------")





