class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def dfs(i, cap):
            if i == len(profit):
                return 0

            if (i, cap) in memo:
                return memo[(i, cap)]

            memo[(i, cap)] = dfs(i+1, cap)

            if cap >= weight[i]:
                memo[(i, cap)] = max(dfs(i+1, cap), dfs(i+1, cap - weight[i]) + profit[i])

            return memo[(i, cap)]

        return dfs(0, capacity)
