import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # for k in range(1, max(piles) + 1):
        #     total_hour = 0
        #     for pile in piles:
        #          total_hour += math.ceil(pile/k)
        #     if total_hour <= h:
        #         return k

        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2
            total_hour = 0
            for pile in piles:
                 total_hour += math.ceil(pile/k)

            if total_hour > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1

        return res
            


