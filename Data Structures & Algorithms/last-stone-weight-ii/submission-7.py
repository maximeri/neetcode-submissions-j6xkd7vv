class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = stone_sum // 2
        # memo = {}

        # def dfs(i, cur_sum):
        #     if i == len(stones):
        #         return abs(stone_sum - 2 * cur_sum)

        #     if (i, cur_sum) in memo:
        #         return memo[(i, cur_sum)]

        #     memo[(i, cur_sum)] = min(dfs(i+1, cur_sum), dfs(i+1, cur_sum + stones[i]))

        #     return memo[(i, cur_sum)]

        # return dfs(0, 0)

        #     [2, 3,1]
        #     0 1 2 3 
        # 0   0 0 0 0 
        # 1   1 
        # 2
        # 3

        dp = defaultdict(int)
        dp[0] = 0

        for stone in stones:
            new_dp = defaultdict(int)
            for j in range(target+1):
                if j >= stone:
                    new_dp[j] = max(dp[j], dp[j-stone] + stone)
                else:
                    new_dp[j] = dp[j]
            dp = new_dp



        stone_sum = sum(stones)
        return abs(dp[target] * 2 - stone_sum)



            

            