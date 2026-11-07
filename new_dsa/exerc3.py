class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        lista2= []


        for conta in accounts:
            lista2.append(sum(conta))

        maio_num = lista2[0]

        for maior in lista2:
            if maior > maio_num:
                maio_num = maior

        return maio_num

rico= Solution()
accs= [[1,5],[7,3],[3,5]]

print(rico.maximumWealth(accs))