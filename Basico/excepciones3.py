def evalua_edad(edad):
    if edad < 0:
        raise NameError("La edad no puede ser menor a 0") #Creamos nuestra propia excepción personalizada, puede ser de cualquier tipo
    elif edad < 20:
        return "Eres joven"
    elif edad < 50:
        return "Eres maduro"

#Esta excepción tiene que ser igual a la excepcion raise, o el programa lanzará la excepción raise y no ejecutará las siguientes líneas de código
try:
    print(evalua_edad(-15))
except NameError as ExcepcionCreada: #Creamos un alias a la excepción
    print(ExcepcionCreada)

print("Más líneas de código")
