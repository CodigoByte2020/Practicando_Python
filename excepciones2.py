def division():

    try:
        valor1 = float(input("Ingrese el primer valor: "))
        valor2 = float(input("Ingrese el segundo valor: "))
        print("El resultado de la división es: " + str(valor1 / valor2))

    # except ValueError:
    #     print("Valor erroneo, ingrese un valor flotante")
    # except ZeroDivisionError:
    #     print("No se puede dividir por cero")

    #except: #Capturamos las excepciones de manera general
    #    print("Se ha producido un error")

    # Cuando un try no tiene except, y si tiene finally, este finally se ejecuta antes de que se lanze el error
    finally:
        print("Operación exitosa")

division()

#Posibles escencarios
#TRY - EXCEPT - FINALLY
#TRY - EXCEPT
#TRY - FINALLY
