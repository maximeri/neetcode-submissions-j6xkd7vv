class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        # 2D dp[i][j] 手裡拿著 s 的第 i 個字，目標是拼出 t 的前 j 個字，共有多少種方法

        # dp[i+1][j+1] = dp[i][j] + dp[i-1][j] # skip + use

        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s)):
            dp[i][0] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                # 情況 A：跳過 s[i-1]。不論是否匹配，我都可以直接繼承「沒用這個字」之前的結果
                dp[i][j] = dp[i-1][j]
                # 情況 B：使用 s[i-1] 來匹配。加上「能拼出目標前綴」的方法數
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[len(s)][len(t)]

