class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # recursive
        # time: n * n! space: n * n!

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
                    if position < len(p) and nums[i] == p[position]:
                        break
            return res

        return helper(0)