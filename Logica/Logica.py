class Logica:
    pass

#     def condicional_unalinea(self):
#         sexo = False
#         sexo = "Masculino" if sexo else "Femenino"
#         return sexo
#
# objeto = Logica()
# print(objeto.condicional_unalinea())
#
# print("*********************************************************")
#
# orientacion = ("Gay", "Lesbiana")
# posicion = True
# definicion = orientacion[not posicion]
# print(definicion)
#
# print("*********************************************************")

curso = input("Ingrese un curso: ")
nivel = "basico"

if curso in ("matemáticas", "algoritmos", "historia"):
    print("Curso {0} nivel {1} seleccionado".format(curso, nivel))
    print("Curso %s nivel %s seleccionado" % (curso, nivel))  # usada en kazator
    print(f'Curso {curso} nivel {nivel} seleccionado')
else:
    raise ValueError()
