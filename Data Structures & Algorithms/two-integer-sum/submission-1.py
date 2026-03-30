class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}

        for i in range(len(nums)):
            if target - nums[i] in sumMap:
                return [sumMap[target - nums[i]], i]
            sumMap[nums[i]] = i


