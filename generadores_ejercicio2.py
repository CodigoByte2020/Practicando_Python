#ejercicio generador yield from

def nombre_paises(*paises):
    for i in paises:
        #for j in i:
        yield from i

ogi = nombre_paises('Perú', 'Colombia', 'Argentina')

print(next(ogi))
print('----------------------------------------------')
print(next(ogi))

# ---------------------------------------- OK ------------------------------------------------