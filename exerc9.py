tuplas = [(2, 8), (4, 5, 6), (1, 2)]

media = list(map(lambda x: (x, sum(x) / len(x)), tuplas))

filtroMedia = list(map(lambda y: y[0], filter(lambda x: x[1] >= 5, media)))

print(filtroMedia)