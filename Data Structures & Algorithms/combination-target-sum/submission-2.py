class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return
            if total > target or i >= len(nums):
                return

            combo.append(nums[i])
            dfs(i, combo, nums[i] + total)
            combo.pop()
            dfs(i+1, combo, total)

        dfs(0, [], 0)
        return res





