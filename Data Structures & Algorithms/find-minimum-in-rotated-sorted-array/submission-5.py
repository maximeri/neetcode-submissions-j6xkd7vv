class Solution:
    def findMin(self, nums: List[int]) -> int:
        # inclusive
        # if len(nums) == 0:
        #     return
        
        # lo, hi = 0, len(nums) - 1
        # res = nums[0]
        # while lo <= hi:
        #     mid = (lo + hi)// 2
        #     if nums[mid] >= nums[lo]:
        #         res = min(nums[lo], res)
        #         lo = mid + 1
        #     else:
        #         res = min(nums[mid], res)
        #         hi = mid - 1
        # return res

        # open-half (lower bound, 
        # finding the smallest one that is equal to or larger than)
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi)// 2
            if nums[mid] <= nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]
            