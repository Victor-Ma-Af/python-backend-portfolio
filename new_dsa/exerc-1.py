class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        cont= 0

        for num  in nums:
            if len(str(num)) %2 == 0:
                cont+=1

        return cont

test_list= Solution()
lista_test= [12, 345, 2, 6, 7896]
print(test_list.findNumbers(lista_test))