class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, n in enumerate(nums):
            if target - n in h:
                return [h[target - n], i]
            h[n] = i
                
