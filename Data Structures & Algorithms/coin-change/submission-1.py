class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, curAmount):
            if curAmount == amount:
                return 0

            if (i, curAmount) in cache:
                return cache[(i, curAmount)]

            if i == len(coins) or curAmount > amount:
                return float('inf')

            cache[(i, curAmount)] = dfs(i+1, curAmount)

            if curAmount + coins[i] <= amount:
                cache[(i, curAmount)] = min(cache[(i, curAmount)], 1 + dfs(i, curAmount + coins[i]))

            return cache[(i, curAmount)]

        ans = dfs(0, 0)
        
        return ans if ans != float('inf') else -1


            
