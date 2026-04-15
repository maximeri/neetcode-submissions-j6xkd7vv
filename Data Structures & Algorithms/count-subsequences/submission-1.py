class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        memo = {}

        def dfs(si, ti):
            if ti == len(t):
                return 1

            if si == len(s):
                return 0

            if (si, ti) in memo:
                return memo[(si, ti)]

            memo[(si, ti)] = dfs(si + 1, ti)
            
            if s[si] == t[ti]:
                memo[(si, ti)] += dfs(si + 1, ti + 1)

            return memo[(si, ti)]

        return dfs(0, 0)
