class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        memo = {}
        def dfs(i, cap):
            if i == n:
                return 0

            if (i, cap) in memo:
                return memo[(i, cap)]

            memo[(i, cap)] = dfs(i+1, cap)

            if cap >= weight[i]:
                memo[(i, cap)] = max(memo[(i, cap)], dfs(i, cap - weight[i]) + profit[i])

            return memo[(i, cap)]

        return dfs(0, capacity)

            