class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max(positive contiguous, even negative, n)
        curMax = curMin = globalMax = nums[0]
        for i in range(1, len(nums)):
            oldMax = curMax
            # curMax 的三種來源：
            # 1. n 自己 (重新開始)
            # 2. n * curMax (正數乘正數，或負數乘正數變更小)
            # 3. n * curMin (負數乘負數，翻轉成最大)
            curMax = max(nums[i], oldMax * nums[i], curMin * nums[i])
            curMin = min(nums[i], oldMax * nums[i], curMin * nums[i])
            globalMax = max(globalMax, curMax)
        return globalMax



