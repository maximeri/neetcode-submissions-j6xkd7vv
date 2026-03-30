class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [1] * len(nums)
        rightProd = [1] * len(nums)
        res = []

        # left
        for i in range(len(nums)-1):
            leftProd[i+1] = leftProd[i] * nums[i]
        
        # right 
        for i in range(len(nums)-1, 0, -1):
            rightProd[i-1] = rightProd[i] * nums[i]

        for i in range(len(nums)):
            res.append(leftProd[i] * rightProd[i])

        return res