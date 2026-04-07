class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
#  123
#  321
#           0 1 2 3 cap 3
#         0 0 0 0 0
#    3    1 0 0 0 3
#    2 3  2 0 0 2 3
#  1 2 3  3 0 2
#         weight

        dp = [0] * (capacity + 1)

        for i in range(len(profit)):
            for j in range(capacity, weight[i]-1, -1):
                dp[j] = max(dp[j], dp[j-weight[i]] + profit[i])

        return dp[capacity]


