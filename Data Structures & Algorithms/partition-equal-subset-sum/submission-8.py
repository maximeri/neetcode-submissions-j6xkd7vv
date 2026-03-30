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
            for j in range(1, target + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i]]

        return dp[len(nums)-1][target]

