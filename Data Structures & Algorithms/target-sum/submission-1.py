class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, curSum):
            if i == len(nums):
                return curSum == target
           
            return dfs(i+1, curSum - nums[i]) + dfs(i + 1, curSum + nums[i])

        return dfs(0, 0)