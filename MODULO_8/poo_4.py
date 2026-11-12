nomes = ["Carlos", "Ana", "João", "Ana", "Carlos", "João", "Ana", "Carlos", "Ana", "Carlos"]
dict_name = {}

for name in range(len(nomes)):
    if nomes[name] not in dict_name:
        dict_name[nomes[name]] = 1
    else:
        dict_name[nomes[name]] += 1

print(dict_name)