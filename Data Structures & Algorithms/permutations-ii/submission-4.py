class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            newPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, num)
                    newPerms.append(pCopy)
                    if i < len(p) and p[i] == num:
                        break
                    
            perms = newPerms


        return perms