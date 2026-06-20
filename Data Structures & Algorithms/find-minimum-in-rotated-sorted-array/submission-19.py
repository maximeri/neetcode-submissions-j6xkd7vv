class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            # 答案可能在 右半邊 所以不可排除 m
            if nums[r] > nums[m]:
                r = m
            else:
                l = m + 1

        return nums[l]