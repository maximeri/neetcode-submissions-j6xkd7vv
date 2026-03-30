class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        def dfs(i, capacity):
            if i == len(profit):
                return 0
            pick = dfs(i+1, capacity)

            # skip
            skip = 0
            newCap = capacity - weight[i]
            if newCap >= 0: 
                skip = profit[i] + dfs(i+1, newCap)

            max_p = max(pick, skip)

            return max_p

        return dfs(0, capacity)