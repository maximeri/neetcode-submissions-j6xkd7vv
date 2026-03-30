class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #  day [r][c] minCost
        n = len(days)
        minCost = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            res = costs[0] + minCost[i+1]

            curIdx = i
            while curIdx < n and days[curIdx] < days[i] + 7:
                curIdx += 1

            res = min(res, costs[1] + minCost[curIdx])

            curIdx = i
            while curIdx < n and days[curIdx] < days[i] + 30:
                curIdx += 1

            res = min(res, costs[2] + minCost[curIdx])

            minCost[i] = res

        return minCost[0]




        # 1 2 4 