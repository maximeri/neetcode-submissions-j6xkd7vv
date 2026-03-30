class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1
        dp = [[0] * cols for _ in range(rows)]
        
        for r in range(1, rows):
            for c in range(1, cols):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
                    
        return dp[rows-1][cols-1]
                

     

        