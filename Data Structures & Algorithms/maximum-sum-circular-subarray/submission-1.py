class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = nums[0]
        curMax = globalMax = nums[0]
        curMin = globalMin = nums[0]
        for n in nums[1:]:
            totalSum += n
            curMax = max(curMax + n, n)
            globalMax = max(globalMax, curMax)
            curMin = min(curMin + n, n)
            globalMin = min(globalMin, curMin)

        # 如果 globalMax < 0，代表整個陣列都是負數
        # 此時直接回傳 globalMax 即可
        if globalMax < 0:
            return globalMax

        return max(globalMax, totalSum - globalMin)
