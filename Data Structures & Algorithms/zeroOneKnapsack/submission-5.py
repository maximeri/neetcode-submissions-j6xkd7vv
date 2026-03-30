class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        def dfs(i, capacity):
            if i == len(profit):
                return 0
            
            if cache[i][capacity] != -1:
                return cache[i][capacity]

            # skip
            skip = dfs(i+1, capacity)

            # choose
            choose = 0
            newCap = capacity - weight[i]
            if newCap >= 0:
                choose = profit[i] + dfs(i+1, newCap)

            cache[i][capacity] = max(skip, choose)

            return cache[i][capacity]
       
        return dfs(0, capacity)
            
