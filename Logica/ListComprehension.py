# def enviar_parametro():
#     lista = []
#     return lista
#
#
# def list_comprehension(lis):
#     for i in range(1, 20, 1):
#         if i % 2 == 0:
#             lis.append(i)
#     return lis
#
#
# print(list_comprehension(enviar_parametro()))
#
# listilla = [i for i in range(1, 31) if not i % 2 and 2 <= i <= 15 or i == 20]
# print(listilla)
# tupl = (1,)  # Si una tupla tiene un solo elemento, esta tiene que llevar una coma en su interior
# print(tupl)
# lis = [3, 5, 6]
# tupla = tuple(rec for rec in range(len(lis)) if rec % 2 == 0)
# print(tupla)


futbolistas = ('Messi', 'Ronaldo', 'Suaréz', 'Gallese')
fut = {key: value for key, value in enumerate(futbolistas)}  # enumerate se aplica sobre una lista o una tupla - Objetos iterables

for i in fut:
    print('Clave: %s, Valor: %s' % (i, fut.get(i)) if i < len(fut) else None)

