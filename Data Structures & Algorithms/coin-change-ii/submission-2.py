class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if total == amount:
                return 1

            if i >= len(coins):
                return 0
            
            skip = dfs(i+1, total)

            choose = 0
            if total + coins[i] <= amount:
                choose = dfs(i, total + coins[i])

            memo[(i, total)] = skip + choose

            return memo[(i, total)]

        return dfs(0, 0)