class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curSet = [], []

        def helper(i, subsets, curSet, nums):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            curSet.append(nums[i])
            helper(i + 1, subsets, curSet, nums)
            curSet.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
                
            helper(i + 1, subsets, curSet, nums)

        helper(0, subsets, curSet, nums)

        return subsets




