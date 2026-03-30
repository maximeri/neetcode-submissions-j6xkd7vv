class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # cache = {}
        # def dfs(i, curAmount):
        #     if curAmount == amount:
        #         return 0

        #     if (i, curAmount) in cache:
        #         return cache[(i, curAmount)]

        #     if i == len(coins) or curAmount > amount:
        #         return float('inf')

        #     cache[(i, curAmount)] = dfs(i+1, curAmount)

        #     if curAmount + coins[i] <= amount:
        #         cache[(i, curAmount)] = min(cache[(i, curAmount)], 1 + dfs(i, curAmount + coins[i]))

        #     return cache[(i, curAmount)]

        # ans = dfs(0, 0)
        
        # return ans if ans != float('inf') else -1

        # tabulation
        # minCoins: min coins to take to reach the c amount
        # r: i's coin, c: amount
        minCoins = [[float("inf")] * (amount + 1) for _ in range(len(coins)+1)]
        for i in range(len(coins) + 1):
            minCoins[i][0] = 0
        for i in range(1, len(coins) + 1):
            for a in range(1, amount + 1):
                minCoins[i][a] = minCoins[i-1][a]
                if a >= coins[i-1]:
                    minCoins[i][a] = min(minCoins[i][a], 1 + minCoins[i][a - coins[i-1]])

        ans = minCoins[len(coins)][amount]
        return ans if ans != float('inf') else -1





            
