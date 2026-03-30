# Hsuan Hsuan
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo)// 2
            print(mid, lo, hi)
            if nums[mid] == target:
                return mid

                        # Left half is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1   # target in left half
                else:
                    lo = mid + 1   # target in right half
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1   # target in right half
                else:
                    hi = mid - 1   # target in left half

        return -1
