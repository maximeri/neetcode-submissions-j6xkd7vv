class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastday = days[len(days) - 1]
        n = len(days)
        memo = {}
        def dfs(i):
            if i == n:
                return 0

            if i in memo:
                return memo[i]

            # choose 1
            res = dfs(i+1) + costs[0]

            # choose 7
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            res = min(res, dfs(j) + costs[1])

            # choose 30
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            res = min(res, dfs(j) + costs[2])

            memo[i] = res

            return memo[i]

        return dfs(0)
            


            
