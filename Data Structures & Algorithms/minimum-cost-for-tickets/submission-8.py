class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 1)
        dp[0] = 0

    #   0 1 4 6
    #   0 1 
    # dp[0]：0 趟旅行（沒出門，花費 0 元）。
    # dp[1]：第 1 趟旅行，對應的日期是 days[0]
    # dp[i]：第 i 趟旅行，對應的日期是 days[i-1]


        for i in range(1, n+1):
            dp[i] = dp[i-1] + costs[0]

            j = i - 1
            while j > 0 and days[j-1] > days[i - 1] - 7:
                j -= 1
            dp[i] = min(dp[i], dp[j] + costs[1])

            j = i - 1
            while j > 0 and days[j-1] > days[i - 1] - 30:
                j -= 1
            dp[i] = min(dp[i], dp[j] + costs[2])

        return dp[n]
       
        # def dfs(i):
        #     if i == n:
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     # choose 1
        #     res = dfs(i+1) + costs[0]

        #     # choose 7
        #     j = i
        #     while j < n and days[j] < days[i] + 7:
        #         j += 1
        #     res = min(res, dfs(j) + costs[1])

        #     # choose 30
        #     j = i
        #     while j < n and days[j] < days[i] + 30:
        #         j += 1
        #     res = min(res, dfs(j) + costs[2])

        #     memo[i] = res

        #     return memo[i]

        # return dfs(0)
            


            
