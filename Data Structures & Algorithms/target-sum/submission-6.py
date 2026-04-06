class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cols = sum(nums) * 2 + 1
        mid = sum(nums)
        dp = defaultdict(int)
        dp[mid] = 1

        for i, num in enumerate(nums):
            new_dp = defaultdict(int)
            for c in range(cols):
                left = dp[c + num] if c + num <= cols else 0 
                right = dp[c - num] if c - num >= 0 else 0
                new_dp[c] = left + right
            dp = new_dp

        return dp[target+mid]

