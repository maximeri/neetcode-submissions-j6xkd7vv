class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for r in range(1, len(nums)):
            if nums[r-1] == nums[r]:
                return True

        return False