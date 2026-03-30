# Hsuan Hsuan
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # initial thought
        # start with left, right most
        # check which is smaller
        # take the smaller half
        # no the condition is wrong

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi)// 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]

