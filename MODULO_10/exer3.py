'''Crie um dicionário contendo quantas vezes cada nome aparece, percorrendo a lista uma única vez.'''

nomes = ["Ana", "João", "Ana", "Carlos", "João", "Ana"]

def qtd_map(interable):

    qtd_repetições = {}

    for name in range(len(interable)):
        if interable[name] not in qtd_repetições:
            qtd_repetições[interable[name]] = 1
        else:
            qtd_repetições[interable[name]] += 1
    return qtd_repetições

nomes = ["Ana", "João", "Ana", "Carlos", "João", "Ana"]

print(qtd_map(nomes))