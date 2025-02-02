lista = [1, 2, 3, 4, 8, 9]

listaPares = list(filter(lambda x : not x % 2, lista))

print(listaPares)