class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lista_2 = []
        somas= 0

        for num in nums:
            soma= num + somas
            lista_2.append(soma)
            somas= soma
        return lista_2

resultado = Solution()
nums= [1, 2, 3, 4, 5]
print(resultado.runningSum(nums))
