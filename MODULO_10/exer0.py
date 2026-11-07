# Exercício 1: O Clássico "Two Sum" (Dois Números)

precos = [200, 1000, 2900, 3300, 4700]
credito_alvo = 3900 # (1000 + 2900)
maps = {}
target = []
for num in range(len(precos)):
    maps[3900- precos[num]] = num
    if 3900- precos[num] in precos:
        target.append(num)
        


print(maps)
print(target)