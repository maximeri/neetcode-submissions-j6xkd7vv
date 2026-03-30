class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if total == amount:
                return 1
            if i >= n or total > amount:
                return 0
            
            choose = dfs(i, total + coins[i])
            skip = dfs(i+1, total)

            memo[(i, total)] = choose + skip

            return memo[(i, total)]

        return dfs(0, 0)
