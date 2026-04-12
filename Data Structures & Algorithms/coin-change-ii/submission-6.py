class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, cur_amount):
            if cur_amount == amount:
                return 1

            if i == len(coins) or cur_amount > amount:
                return 0
            
            if (i, cur_amount) in memo:
                return memo[(i, cur_amount)]

            memo[(i, cur_amount)] = dfs(i, cur_amount + coins[i]) + dfs(i + 1, cur_amount)

            return memo[(i, cur_amount)]
            
        return dfs(0, 0)



        