from functools import reduce

lista = ["casa", "python", "lambda"]

novaLista = reduce(lambda x, y: x + y, map(len, lista))

print(novaLista)