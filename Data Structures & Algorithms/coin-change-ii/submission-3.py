class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # ways to make amount j using i coin
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)] 
        
        for i in range(len(coins)+1):
            dp[i][0] = 1
            
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                # skip
                # 如果不准用 2 元，之前用 1 元湊出 3 元有幾種方法
                dp[i][j] = dp[i-1][j]
                # choose 
                if j >= coins[i-1]:
                    # ways to make amount j using i coin 
                    # 如果用 2 元，剩下的 1 元，有幾種方法達成？
                    dp[i][j] += dp[i][j-coins[i-1]]

        return dp[len(coins)][amount]
