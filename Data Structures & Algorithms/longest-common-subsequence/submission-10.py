class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Ensure text2 is the shorter string to minimize space
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        s1, s2 = len(text1), len(text2)
        dp = [0] * (s2+1)
        for i1 in range(s1):
            prev = 0 # This represents dp[i-1][j-1] (the diagonal)
            for i2 in range(s2):
                temp = dp[i2 + 1] # Store the "top" value before overwriting it
                if text1[i1] == text2[i2]:
                    dp[i2+1] = prev + 1
                else:
                    dp[i2+1] = max(dp[i2+1], dp[i2])
                prev = temp

        return dp[s2]

        
        
        # 2D
        s1, s2 = len(text1), len(text2)
        dp = [[0] * (s2+1) for _ in range(s1+1)] # Watch out for init order!

        for i1 in range(s1):
            for i2 in range(s2):
                if text1[i1] == text2[i2]:
                    dp[i1+1][i2+1] = dp[i1][i2] + 1
                else:
                    dp[i1+1][i2+1] = max(dp[i1][i2+1], dp[i1+1][i2])

        return dp[s1][s2]

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



