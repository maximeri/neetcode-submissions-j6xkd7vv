class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # iterative
        # time: O(n * n!) space: O(n * n!)
        perms = [[]]

        for num in nums:
            newPerms = []
            for p in perms:
                for position in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(position, num)
                    newPerms.append(pCopy)
            perms = newPerms

        return perms
