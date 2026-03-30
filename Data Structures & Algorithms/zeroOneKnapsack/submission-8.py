class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = [[-1] * (capacity+1) for _ in range(len(profit))] # r profit c capacity
        
        def dfs(i, capacity):
            if i == len(profit):
                return 0

            if cache[i][capacity] != -1:
                return cache[i][capacity]

            pick = dfs(i+1, capacity)

            # skip
            skip = 0
            newCap = capacity - weight[i]
            if newCap >= 0: 
                skip = profit[i] + dfs(i+1, newCap)

            cache[i][capacity] = max(pick, skip)

            return cache[i][capacity]

        return dfs(0, capacity)