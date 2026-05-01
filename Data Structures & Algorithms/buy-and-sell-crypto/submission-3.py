class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 2:
            max_profit = prices[1] - prices[0]
            return max_profit if max_profit > 0 else 0

        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

            while prices[l] > prices[r]:
                l += 1

            r += 1

        return max_profit

            