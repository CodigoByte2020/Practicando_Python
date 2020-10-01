#HALLAR PUNTUACIÓN Y SUELDO DE UN TRABAJADOR

puntuacion_usuario = float(input("Ingrese su puntación: "))
nivel = ""
dinero = 0

if puntuacion_usuario == 0.0:
    nivel = "inaceptable"
    dinero = puntuacion_usuario
elif puntuacion_usuario == 0.4:
    nivel = "aceptable"
    dinero = 2400 * puntuacion_usuario
elif puntuacion_usuario >= 0.6:
    nivel = "meritorio"
    dinero = 2400 * puntuacion_usuario

print("Su nivel de rendimiento es " + nivel)
print("La cantidad de dinero que recibirá es: " + str(dinero))
# **************** OK ***********************************************
