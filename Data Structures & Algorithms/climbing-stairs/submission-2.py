class Solution:
    def climbStairs(self, n: int) -> int:
        # s s s s s s

        stairs = [0] * (n+2)
        stairs[0] = 0
        stairs[1] = 1

        for i in range(2, n+2):
            stairs[i] = stairs[i - 1] + stairs[i - 2]
        
        return stairs[n+1]