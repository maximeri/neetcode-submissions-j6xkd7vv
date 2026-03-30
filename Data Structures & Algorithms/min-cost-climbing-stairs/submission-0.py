class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur, nxt = 0, 0
        for i in range(len(cost) - 1):
            tmp = min(cur + cost[i], nxt + cost[i+1])
            cur = nxt
            nxt = tmp
        
        return nxt