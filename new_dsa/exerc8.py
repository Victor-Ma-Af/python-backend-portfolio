class Solution:
    def addDigits(self, num: int) -> int:

        while int(len(str(num)) > 1):
            acum = []
            for char in str(num):
                acum.append(int(char))

            num = sum(acum)

        return num