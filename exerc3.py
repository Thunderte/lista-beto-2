from functools import reduce

lista = [2, 3, 4, 6, 7, 8]

listaSomada = int(reduce(lambda x, y: x + y, lista))

print(listaSomada)