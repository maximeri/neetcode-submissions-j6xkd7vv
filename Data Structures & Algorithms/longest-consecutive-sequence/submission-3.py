class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in nums:
            count = 1
            while num in num_set:
                res = max(res, count)
                count += 1
                num += 1


        return res

        