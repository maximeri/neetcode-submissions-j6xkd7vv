class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        minCost = {}
        # i's day return minCost
        n = len(days)
        def dfs(i):
            if i in minCost:
                return minCost[i]
            if i >= n:
                return 0

            # one day
            minCost[i] = costs[0] + dfs(i+1)

            # 7 day
            curIdx = i
            while curIdx < n and days[curIdx] < days[i] + 7:
                curIdx += 1
            minCost[i] = min(minCost[i], costs[1] + dfs(curIdx))

            # 15 day
            curIdx = i
            while curIdx < n and days[curIdx] < days[i] + 30:
                curIdx += 1
            minCost[i] = min(minCost[i], costs[2] + dfs(curIdx))

            return minCost[i]



        return dfs(0)

           