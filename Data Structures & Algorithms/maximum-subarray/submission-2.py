class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = allTimeMax = nums[0]
        for n in nums[1:]:
            curMax = max(n, n + curMax)
            allTimeMax = max(curMax, allTimeMax)

        return allTimeMax 