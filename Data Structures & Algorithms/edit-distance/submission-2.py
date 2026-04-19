class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i1, i2):
            if (i1, i2) in memo:
                return memo[(i1, i2)]

            if i1 == len(word1):
                return len(word2) - i2

            if i2 == len(word2):
                return len(word1) - i1

            if word1[i1] == word2[i2]:
                return dfs(i1 + 1, i2 + 1)

            memo[(i1, i2)] = 1 + min(
                dfs(i1 + 1, i2),      # Delete from word1
                dfs(i1, i2 + 1),      # Insert into word1 (matches word2[j])
                dfs(i1 + 1, i2 + 1)   # Replace word1[i] with word2[j]
            )

            return memo[(i1, i2)]

        return dfs(0, 0)


            
