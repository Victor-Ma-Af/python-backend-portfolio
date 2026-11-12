'''Exercício 9 — Remover duplicatas
Receba uma lista de IDs de usuários e retorne apenas os IDs únicos, preservando a ordem original.

Desafio: utilize um set para evitar verificações repetidas em toda a lista.'''

ids = [101, 204, 307, 101, 412, 204, 519, 307, 623, 412, 728, 101, 831, 519, 934, 623, 204, 728, 101, 831]   

resultado = []
vistos  = set()

for id in ids:
    if id not in vistos:
        resultado.append(id)
        vistos.add(id)

print(resultado)
