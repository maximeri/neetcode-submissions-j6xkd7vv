class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init with 1 since 0 will make product 0
        res = [1] * len(nums)

        prefix = 1 # 邊界的初始值永遠是 1
        # left of nums[i] product 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # right of nums[i] product
        postfix = 1 # 邊界的初始值永遠是 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res



        


        