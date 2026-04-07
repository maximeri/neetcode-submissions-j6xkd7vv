class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # memo = {}
        # def dfs(i, cap):
        #     if i == len(profit):
        #         return 0

        #     if (i, cap) in memo:
        #         return memo[(i, cap)]

        #     memo[(i, cap)] = dfs(i+1, cap)

        #     if cap >= weight[i]:
        #         memo[(i, cap)] = max(dfs(i+1, cap), dfs(i+1, cap - weight[i]) + profit[i])

        #     return memo[(i, cap)]

        # return dfs(0, capacity)

        dp = [[0] * (capacity + 1) for _ in range(len(profit) + 1)]
        for i in range(1, len(profit) + 1):
            for j in range(1, capacity + 1):
                dp[i][j] = dp[i-1][j]
                if j >= weight[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-weight[i-1]] + profit[i-1])

        return dp[len(profit)][capacity]

