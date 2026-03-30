class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n)]

        # Base case: Target 0 is always possible (by picking nothing)
        for i in range(n):
            dp[i][0] = True

        # # Base case: The first element can fulfill its own target
        # if nums[0] <= target:
        #     dp[0][nums[0]] = True

        for i in range(1, n):
            for t in range(1, target + 1):
                # Option 1: Skip the current number (look at the row above)
                skip = dp[i-1][t]
                
                # Option 2: Take the current number (if it fits)
                take = False
                if t >= nums[i]:
                    take = dp[i-1][t - nums[i]]
                
                dp[i][t] = skip or take

        return dp[n-1][target]