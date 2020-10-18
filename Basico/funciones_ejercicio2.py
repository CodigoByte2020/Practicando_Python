'''Escribir una función que calcule el total de una factura tras aplicarle el IGV. 
La función debe recibir la cantidad sin IGV y el porcentaje de IGV a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IGV, deberá aplicar un 21%.'''

def total_factura(monto_factura, igv):
    total = monto_factura - monto_factura * (igv / 100)
    return total

def total_factura2(monto_factura):
    total = monto_factura - monto_factura  * (21 / 100)
    return total

print('El total de la factura es: ' + str(total_factura(250, 18)))
print('El total de la factura es: ' + str(total_factura2(250)))