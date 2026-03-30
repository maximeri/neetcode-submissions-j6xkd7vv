class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            # 問完所有數字
            if i >= len(nums):
                res.append(subset.copy())
                return
            # i want the number and move on
            subset.append(nums[i])
            dfs(i + 1)

            # i don't want the number and move on
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return res

            
