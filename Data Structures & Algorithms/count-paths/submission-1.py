class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[r][c] = dp[r-1][c] + dp[r][c-1]
        # dp[j] = dp[j] + dp[j-1]
        if n > m:
            m, n = n, m
        dp = n * [1]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]

        return dp[n-1]