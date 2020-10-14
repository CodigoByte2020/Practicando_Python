'''Instruccón yield from en generadores'''

def devuelve_ciudades(*ciudades): #el * nos permite recibir un número indeterminado de elementos en forma de tupla
    for i in ciudades:
        #for j in i:
        yield from i

obj_gen_it = devuelve_ciudades('Lima', 'Bogotá', 'Santiago', 'Quito')
print(next(obj_gen_it))
print(next(obj_gen_it))