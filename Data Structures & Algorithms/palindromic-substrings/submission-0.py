class Solution:
    def countSubstrings(self, s: str) -> int:
        num = len(s)
        
        dp = [[False] * num for _ in range(num)]

        count = 0
        for i in range(num-1, -1, -1):
            for j in range(i, num):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        
        return count