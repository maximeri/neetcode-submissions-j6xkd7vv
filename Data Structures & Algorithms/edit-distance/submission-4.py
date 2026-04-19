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

        dp = [i for i in range(len(word1) + 1)]

        for j in range(1, len(word2) + 1):
            prev = dp[0]
            dp[0] = j
            for i in range(1, len(word1) + 1):
                temp = dp[i]
                if word1[i-1] == word2[j-1]:
                    dp[i] = prev
                else:
                    dp[i] = 1 + min(
                        dp[i-1],    # Delete
                        dp[i],    # Insert
                        prev   # Replace
                    )
                prev = temp

        return dp[len(word1)]



            
