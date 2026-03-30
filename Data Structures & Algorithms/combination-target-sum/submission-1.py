class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curCombo = []

        def dfs(i, curSum):
            if curSum == target:
                res.append(curCombo.copy())
                return
            if curSum > target or i >= len(nums):
                return
            # I want to number and move on
            curCombo.append(nums[i])
            dfs(i, curSum + nums[i])

            # I don't want the number and move on
            curCombo.pop()
            dfs(i + 1, curSum)

        dfs(0, 0)
        return res