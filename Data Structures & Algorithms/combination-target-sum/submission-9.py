class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, curSet):
            if total == target:
                res.append(curSet.copy())
                return

            if i >= len(nums) or total > target:
                return

            curSet.append(nums[i])
            dfs(i, total + nums[i], curSet)
            curSet.pop()
            dfs(i+1, total, curSet)

        dfs(0, 0, [])

        return res

