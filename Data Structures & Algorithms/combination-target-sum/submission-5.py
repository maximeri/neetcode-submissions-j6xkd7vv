class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs, curComb = [], []

        def helper(i, curTarget):
            if curTarget == 0:
                combs.append(curComb.copy())
                return
            
            for j in range(i, len(nums)):
                if curTarget < 0:
                    return
                curComb.append(nums[j])
                curTarget -= nums[j]
                helper(j, curTarget)
                curComb.pop()
                curTarget += nums[j]

        helper(0, target)

        return combs