def separandoNumeros(lista):
    return {
        "positivos": list(filter(lambda x: x > 0, lista)),
        "negativos": list(filter(lambda x: x < 0, lista)),
        "zeros": list(filter(lambda x: x == 0, lista))
    }

lista = [0, 2, -2, 5, 0, -1]

print(separandoNumeros(lista))