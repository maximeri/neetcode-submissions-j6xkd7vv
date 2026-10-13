class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # nums = [1,2,4,6]
        # res = [1, 1, 2, 8] 排除自己左邊乘機
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # nums = [1, 2, 4, 6]
        # left res  = [1, 1, 2, 8] 排除自己左邊乘機
        # final res  = [48, 24, 12, 8]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res