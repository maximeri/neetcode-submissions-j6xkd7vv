class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursive
        # time: O(n*n!) space: O(n!)
        def helper(i):
            if i == len(nums):
                return [[]]

            perms = helper(i+1)
            res = []

            for p in perms:
                for position in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(position, nums[i])
                    res.append(pCopy)
            return res

        return helper(0)