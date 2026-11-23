class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 2 cases
        # 中間一段 maxSum
        # 中間挖空（含頭尾） maxSum total - minSum
        curMin, globalMin = 0, nums[0]
        curMax, globalMax = 0, nums[0]

        for num in nums:
            # 中間挖空
            curMin += num
            globalMin = min(globalMin, curMin)
            curMin = min(0, curMin)

             # 中間一段
            curMax += num
            globalMax = max(globalMax, curMax)
            curMax = max(0, curMax)

        total = sum(nums)

        if total - globalMin == 0:
            return globalMax
        else:
            return max(globalMax, total - globalMin)