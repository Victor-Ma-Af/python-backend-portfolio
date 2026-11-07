class Solution:
    def judgeCircle(self, moves: str) -> bool:

        lR = uD = 0

        for side in moves:
            if side == "L": lR-= 1
            elif side == "R": lR+= 1
            elif side == "U": uD+= 1
            elif side == "D": uD-= 1

        return lR == uD == 0

string = Solution()
moves = "LLRR"

print(string.judgeCircle(moves))