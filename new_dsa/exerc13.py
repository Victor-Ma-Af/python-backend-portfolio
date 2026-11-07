'''
Prograama recebe uma lista de numeros e um valor alvo onde. Na lista o progrma procura qual quer soma de dois numeros
que resulte no alvo e retorna um lista com as posições das somas

# primeiro loop percorre os inteiro da lista, e para cada num indice tem que ser atualizada por representar a posição do primeiro num
# segundo loop for percorrer uma cópia da lista começando sempre pelo próximo caracter depois de num
# se num + num2 for igual a target, adicionar a new os valores atuais dos indices
# indice2 += 1
# indice sem será definido como valor de indice + 1
'''
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indice = 0
        indice2 = 1
        i = 1
        new = []
        for num in nums:
            indice2 = indice + 1
            for num2 in nums[i:]:
                if num + num2 == target:
                    new.append(indice)
                    new.append(indice2)

                indice2 += 1
            i+= 1
            indice+= 1

        return new
'''
