class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        maxProfit = 0

        l, r = 0, 1

        while r < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1

        return maxProfit
            
    
            