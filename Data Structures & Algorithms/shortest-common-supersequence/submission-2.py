class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = str1[:i]
            
        for j in range(1, n + 1):
            dp[0][j] = str2[:j]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    pick_i = dp[i-1][j] + str1[i-1]
                    pick_j = dp[i][j-1] + str2[j-1]
                    if len(pick_i) < len(pick_j):
                        dp[i][j] = pick_i
                    else:
                        dp[i][j] = pick_j

        return dp[m][n]
