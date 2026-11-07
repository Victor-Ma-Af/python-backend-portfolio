class Solution:
    def reverse(self, num: int) -> int:

        absolute_num = lambda num: - num if num < 0 else num
        verify= lambda num: 0 if num < -2**32 or num > 2**32 else num

        new_num= int(str(absolute_num(num))[::-1])* -1

        if num> 0: return verify(new_num)* -1
        else: return verify(new_num)

teste = Solution()

print(teste.reverse(123))