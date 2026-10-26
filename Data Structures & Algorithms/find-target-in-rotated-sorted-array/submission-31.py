class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # 檢查哪一半是有序的
            # 1. 右半邊是有序的
            if nums[m] <= nums[r]:
                # 檢查 target 是否落在有序的右半邊區間內
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # 2. 否則，左半邊一定是有序的
            else:
                # 檢查 target 是否落在有序的左半邊區間內
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1