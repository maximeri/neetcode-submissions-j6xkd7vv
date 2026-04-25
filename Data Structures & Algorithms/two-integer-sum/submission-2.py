class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        halfs = {}

        for i in range(len(nums)):
            if (target - nums[i]) in halfs:
                return [halfs[target - nums[i]], i]
            halfs[nums[i]] = i