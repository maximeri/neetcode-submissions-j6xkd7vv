class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        # 真的只有一列空間
        dp = [0] * (M + 1)

        for i in range(N):
            p, w = profit[i], weight[i]
            # 必須倒著跑，直到裝不下該物品為止
            for j in range(M, w - 1, -1):
                # 這裡的 dp[j-w] 保證是「上一輪」的結果
                dp[j] = max(dp[j], p + dp[j - w])

        return dp[M]