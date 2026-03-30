class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # iterative
        # time: n * n! space: n * n!

        perms = [[]]

        for num in nums:
            newPerms = []
            for p in perms:
                for position in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(position, num)
                    newPerms.append(pCopy)
                    if position < len(p) and p[position] == num:
                        break
            perms = newPerms

        return perms
            