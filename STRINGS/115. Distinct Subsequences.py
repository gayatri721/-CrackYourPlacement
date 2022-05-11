class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        
        # set right column to 1
        for i in range(len(s)+1):
            dp[i][-1] = 1
        
        for i in reversed(range(len(s))):
            for j in reversed(range(len(t))):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][0]
