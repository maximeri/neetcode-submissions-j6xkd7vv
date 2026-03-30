class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # time: 
        # space:

        combs, curComb = [], []

        def helper(i, curComb, target):
            if target < 0:
                return
            
            if target == 0:
                combs.append(curComb.copy())

            for j in range(i, len(nums)):
                curComb.append(nums[j])
                helper(j, curComb, target - nums[j])
                curComb.pop()

        helper(0, curComb, target)
        return combs
