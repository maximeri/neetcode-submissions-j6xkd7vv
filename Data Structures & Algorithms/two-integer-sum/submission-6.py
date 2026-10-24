class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        halfIx = defaultdict(int) # num: idx

        for i in range(len(nums)):
            if target - nums[i] in halfIx:
                return [halfIx[target - nums[i]], i]
            halfIx[nums[i]] = i
