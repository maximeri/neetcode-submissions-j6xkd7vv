class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # cache = {} # use map to avoid negative index
        # def dfs(i, curSum):
        #     if i == len(nums):
        #         return 1 if curSum == target else 0
        #     if (i, curSum) in cache:
        #         return cache[(i, curSum)]
        #     cache[(i, curSum)] = dfs(i+1, curSum - nums[i]) + dfs(i + 1, curSum + nums[i])
        #     return cache[(i, curSum)]
        # return dfs(0, 0)

        # tabultation
        # n = len(nums)
        # dp = [defaultdict(int) for _ in range(n+1)] # i [{total:count}]
        # dp[0][0] = 1

        # for i in range(n):
        #     for total, count in dp[i].items():
        #         dp[i+1][total + nums[i]] += count
        #         dp[i+1][total - nums[i]] += count

        # return dp[n][target]

        # space optimized
        n = len(nums)
        dp = defaultdict(int) # {total:count}
        dp[0] = 1

        for i in range(n):
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total+nums[i]] += count
                next_dp[total-nums[i]] += count
            dp = next_dp

        return dp[target]








        

