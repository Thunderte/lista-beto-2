from functools import reduce

def mediaPonderada(notasAlunos):
    mediasPonderadas = {}
    for aluno, notas in notasAluno.items():
        notasNPeso = notas[:-1]
        pesoNotas = notas[-1]
        soma = reduce(lambda acc, nota: acc + nota * pesoNotas, notasNPeso, 0)
        media = soma / len(notasNPeso)
        mediasPonderadas[aluno] = media
    return mediasPonderadas

# Exemplo de uso
notasAluno = {
    "João": [8, 7, 9, 2],
    "Ana": [5, 6, 7, 3]
}

print(mediaPonderada(notasAluno))