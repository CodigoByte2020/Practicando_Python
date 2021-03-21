# # def potencia(base, exponente):
# #     return base ** exponente
# # print(potencia(5, 2))
# a = None
# # Una función lambda tambien puede no tener parámetros, pero tiene que tener si o si una instrucción
# funcion_lambda = lambda: 5 > 0 and (10 < 2 or a is None)
# print(funcion_lambda())
#
#
# def function_logic():
#     return not funcion_lambda()
#
# print(function_logic())


# Closure: son funciones que dentro de ellas definen otras funciones

def funcion1(tupla):
    n1, n2, n3 = tupla
    lista = list(range(n1, n2, n3))

    def validar_lista():
        return len(lista) == 5
    # print('La lista tiene 5 elementos.') if validar_lista() else None
    return validar_lista()


def funcion2(n1, n2, n3):
    return n1, n2, n3  # Esta función retorna una tupla


print('La lista tiene 5 elementos.') if funcion1(funcion2(1, 10, 2)) else None
