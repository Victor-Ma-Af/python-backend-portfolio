'''
Programa recebe uma lista NÃO decresente de numeros, remove todas as repetições e adiciona "_" para cada duplicata removida. Ao final retorna a quantidade de numeros da lista

-contar as duplicatas
    -criar um set baseada na lsita principal medir o tamanho do conjunto(set)
    -comparar com o tamnho da lista original
-remover as duplicatas
-adicionar qtd de "_" equivalentes a qtd de duplicatas
-conta os elementos da lista

'''
nums = [0,0,1,1,1,2,2,3,3,4]
i = 1

for j in range(1, len(nums)):
    if nums[j] != nums[j-1]:
        nums[i] = nums[j]
        i += 1



print(nums)