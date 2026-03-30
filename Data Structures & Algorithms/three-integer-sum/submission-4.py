# Hsuan Hsuan review
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        exist = {}
        for i in range(len(nums)):
            target = (-1)*nums[i]
            mp = {}
            for j in range(i+1, len(nums)):
                pos = sorted([nums[i], target - nums[j], nums[j]])
                if target - nums[j] in mp and tuple(pos) not in exist:
                    res.append(pos)
                    exist[tuple(pos)] = True
                mp[nums[j]] = j 
        return res