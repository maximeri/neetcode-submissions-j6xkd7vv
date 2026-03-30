class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity

        dp = [0] * (M + 1)

        for cap in range(M + 1):
            if weight[0] <= cap:
                dp[cap] = profit[0]
        
        for i in range(1, N):
            curRow = [0] * (M + 1)
            for cap in range(1, M + 1):
                skip = dp[cap]
                pick = 0
                if cap - weight[i] >= 0:
                    pick = profit[i] + dp[cap - weight[i]]
                curRow[cap] = max(pick, skip)
            dp = curRow

        return dp[M]

                
