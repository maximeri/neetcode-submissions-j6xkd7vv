class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = []
        res = []
        for r in range(len(nums)):
            if r - l + 1 == k:
                window = nums[l:r+1]
                res.append(max(window))
                l += 1

        return res
            

