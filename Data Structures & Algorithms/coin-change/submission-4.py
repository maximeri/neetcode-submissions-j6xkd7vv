import sys
sys.setrecursionlimit(15000)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        n = len(coins)
        
        def dfs(i, cur_amount):
            if i == n:
                return float('inf')
            if cur_amount == amount:
                return 0 
           
            if (i, cur_amount) in memo:
                return memo[(i, cur_amount)]

            memo[(i, cur_amount)] = dfs(i+1, cur_amount)

            if cur_amount + coins[i] <= amount:
                memo[(i, cur_amount)] = min(memo[(i, cur_amount)], dfs(i, cur_amount + coins[i])+1)
            
            return memo[(i, cur_amount)]

        res = dfs(0, 0)
        
        # 如果結果是無限大，代表湊不出來，回傳 -1
        return res if res != float('inf') else -1