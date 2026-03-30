class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        def dfs(i, capacity):
            if i == len(profit):
                return 0

            # skip item i
            res_skip = dfs(i + 1, capacity)


            # include
            res_incl = 0
            if capacity - weight[i] >= 0:
                res_incl = profit[i] + dfs(i + 1, capacity - weight[i])


            return max(res_skip, res_incl)


        return dfs(0, capacity)