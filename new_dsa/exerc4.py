class Solution:
    def calPoints(self, operations: List[str]) -> int:

        teste2 = []

        for num in operations:
            try:
                teste2.append(int(num))

            except ValueError:
                if num == "+":
                    teste2.append(teste2[-2]+teste2[-1])
                elif num == "C":
                    teste2.remove(teste2[-1])
                elif num == "D":
                    teste2.append(teste2[-1] *2)
        

        return sum(teste2)


points = Solution()
operatio = ["5","-2","4","C","D","9","+","+"]

print(points.calPoints(operatio))