class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        
        # dp = [0] * (len(t) + 1)

        # for sc in s:
        #     prev = 0
        #     for ti in range(len(t)):
        #         tmp = dp[ti + 1]
        #         if t[ti] == sc:
        #             dp[ti + 1] = prev + 1
        #         else:
        #             dp[ti + 1] = max(dp[ti + 1], dp[ti])
        #         prev = tmp

        # return dp[len(t)]

        memo = {}

        def dfs(si, ti):
            if (si, ti) in memo:
                return memo[(si, ti)]

            if ti == len(t):
                return 1

            if si == len(s):
                return 0

            if s[si] == t[ti]:
                memo[(si, ti)] =  dfs(si + 1, ti + 1) + dfs(si + 1, ti)
            else:
                memo[(si, ti)] = dfs(si+1, ti)

            return memo[(si, ti)]
            
        return dfs(0, 0)
