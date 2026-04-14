class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1, s2 = len(text1), len(text2)
        memo = {}
        
        def dfs(i1, i2):
            if i1 == s1 or i2 == s2:
                return 0

            if (i1, i2) in memo:
                return memo[(i1, i2)]

            # match
            if text1[i1] == text2[i2]:
                memo[(i1, i2)] = 1 + dfs(i1 + 1, i2 + 1)
            else:
                # not match
                memo[(i1, i2)] = max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))

            return memo[(i1, i2)]

        return dfs(0, 0)
