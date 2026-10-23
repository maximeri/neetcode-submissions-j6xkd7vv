class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1

        # left part
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        # [1, 1, 2, 8]

        # [1,2,4,6]

        # [48,24,12,8]

        prefix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= prefix
            prefix *= nums[i]

        return result
