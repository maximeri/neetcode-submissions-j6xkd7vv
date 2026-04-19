class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 2D
    #     x a b
    # x   0
    # a   1
    # a   2
    # b   3

        if len(word1) > len(word2):
            word1, word2 = word2, word1

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i

        for j in range(len(word2) + 1):
            dp[0][j] = j

        for j in range(1, len(word2) + 1):
            for i in range(1, len(word1) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # Delete
                        dp[i][j-1],    # Insert
                        dp[i-1][j-1]   # Replace
                    )

        return dp[len(word1)][len(word2)]



            
