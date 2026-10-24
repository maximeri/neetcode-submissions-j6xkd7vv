class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 尋找它右邊有沒有兩個數能和它相加等於 0
        nums.sort() # [-4, -1, -1, 0, 1, 2] 
        

        res = []
        for i in range(len(nums) - 2):
            # [-1, -1, 0, 1]
            if i > 0 and nums[i] == nums[i-1]: 
                continue 
            l, r = i + 1, len(nums) - 1 

            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    # [-2, 0, 0, 2, 2]
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1 
                    l += 1
                    r -= 1
                   

        return res


