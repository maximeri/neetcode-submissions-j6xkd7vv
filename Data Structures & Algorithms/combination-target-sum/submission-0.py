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
           
            curCombo.append(nums[i])
            dfs(i, curSum + nums[i])

            curCombo.pop()
            dfs(i + 1, curSum)

        dfs(0, 0)
        return res