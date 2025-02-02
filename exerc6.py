def retornaDicionario(lista):
   return {
      "pares": list(filter(lambda x: not x % 2, lista)),
      "impares": list(filter(lambda x: x % 2, lista))
   }

lista = [2, 4, 6, 5, 10, 12, 15]

print(dict(retornaDicionario(lista)))