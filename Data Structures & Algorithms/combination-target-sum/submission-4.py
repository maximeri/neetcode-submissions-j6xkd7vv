class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs, curComb = [], []

        def helper(i, combs, curComb, nums, target):
            if sum(curComb) == target:
                combs.append(curComb.copy())
                return

            for j in range(i, len(nums)):
                if sum(curComb) > target:
                    return
                curComb.append(nums[j])
                helper(j, combs, curComb, nums, target)
                curComb.pop()

        helper(0, combs, curComb, nums, target)

        return combs
            