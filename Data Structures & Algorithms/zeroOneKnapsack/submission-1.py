class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(i, capacity):
            if i == len(profit):
                return 0

            # skip
            skip = dfs(i+1, capacity)

            # choose
            newCap = capacity - weight[i]
            choose = 0
            if newCap >= 0:
                choose = profit[i] + dfs(i+1, newCap)

            return max(skip, choose)

        return dfs(0, capacity)
            
