#EL PRECIO DE LAS FRUTAS
diccionario = {"plátano": 1.35, "manzana": 0.80, "pera": 2, "naranja": 0.70}
fruta = input("¿Que fruta deseas comprar? ")
kilos = float(input("¿Cuántos kilos deseas? "))


if fruta in diccionario: #Se busca la clave, mas no el valor
    print(f"{kilos} Kg de {fruta} valen {(diccionario[fruta] * kilos)} soles")
else:
    print("La fruta que desea no está disponible")

#************************************ OK *********************************************
