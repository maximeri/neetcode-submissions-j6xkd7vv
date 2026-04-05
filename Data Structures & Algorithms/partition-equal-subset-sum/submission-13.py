class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %  2 > 0:
            return False

        n = len(nums)
        target = sum(nums) // 2
        memo = {}

        def dfs(i, total):
            if total == target:
                return True

            if (i, total) in memo:
                return memo[(i, total)]

            if i == n:
                return False

            memo[(i, total)] = dfs(i+1, total)

            if nums[i] + total <= target:
                memo[(i, total)] = dfs(i+1, total + nums[i]) or memo[(i, total)]

            return memo[(i, total)]

        return dfs(0, 0)