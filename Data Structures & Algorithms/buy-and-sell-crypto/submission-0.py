# Hsuan Hsuan
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initial thought
        # hold the current lowest price and the largest profit
        if len(prices) == 0:
            return 0
        lo = prices[0]
        profit = -1
        for p in prices:
            if p < lo:
                lo = p
            if p - lo > profit:
                profit = p - lo
        return profit