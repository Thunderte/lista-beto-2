listaNomes = ["Ana", "Lucas", "Fernanda", "João"]

nomesFiltrados = list(filter(lambda x: len(x) >= 5, listaNomes))

print(nomesFiltrados)