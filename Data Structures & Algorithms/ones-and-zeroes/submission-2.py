class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cost = [{"0": 0, "1": 0} for _ in range(len(strs))]
        for index, chars in enumerate(strs):
            for c in chars:
                if c == "0":
                    cost[index]["0"] += 1
                if c == "1":
                    cost[index]["1"] += 1

        # memo = {}
        # def dfs(i, cur_m, cur_n):
        #     if i == len(strs):
        #         return 0

        #     if (i, cur_m, cur_n) in memo:
        #         return memo[(i, cur_m, cur_n)]

        #     memo[(i, cur_m, cur_n)] = dfs(i+1, cur_m, cur_n)

        #     if cur_m - cost[i]["0"] >= 0 and cur_n - cost[i]["1"] >= 0:
        #         memo[(i, cur_m, cur_n)] = max(memo[(i, cur_m, cur_n)], 1 + dfs(i+1, cur_m - cost[i]["0"], cur_n - cost[i]["1"]))

        #     return memo[(i, cur_m, cur_n)]

        # return dfs(0, m, n)

    #     0 1 capacity
    #   0 0 0
    #   1 0 1
    #   1 
    #   item

        dp = [[0] * (n + 1) for _ in range(m+1)]
        
        for i in range(len(cost)):
            cost_zero = cost[i]["0"]
            cost_one = cost[i]["1"]
            for j in range(m, cost_zero-1, -1):
                for k in range(n, cost_one-1, -1):
                    if j >= cost_zero and k >= cost_one:
                        dp[j][k] = max(dp[j][k], dp[j-cost_zero][k-cost_one] + 1)

        return dp[m][n]

    


            