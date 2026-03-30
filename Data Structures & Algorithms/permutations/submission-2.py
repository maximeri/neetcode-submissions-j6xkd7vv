class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return[[]]

        def helper(i):
            if i == len(nums):
                return [[]]

            perms = helper(i+1)
            res = []
            
            for p in perms:
                for j in range(len(p) + 1): # 尋找所有可能的縫隙
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res
        
        return helper(0)
        


