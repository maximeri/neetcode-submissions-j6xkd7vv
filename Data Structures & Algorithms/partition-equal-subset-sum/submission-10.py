class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [[False] * (target + 1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True

        for i in range(1, len(nums)):
            for t in range(1, target + 1):
                # if nums[i] == t:
                #     dp[i][t] = True
                skip = dp[i-1][t] # can we sum to target using previous items
                take = False
                if t >= nums[i]:
                    take = dp[i-1][t-nums[i]]
                dp[i][t] = skip or take

        return dp[len(nums)-1][target]

