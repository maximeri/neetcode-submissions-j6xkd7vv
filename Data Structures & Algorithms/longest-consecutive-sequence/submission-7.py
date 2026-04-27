class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in nums:
            if num not in num_set:
                continue
                
            count = 1
            left, right = num - 1, num + 1
            while left in num_set:
                num_set.remove(left)
                count += 1
                left -= 1

            while right in num_set:
                num_set.remove(right)
                count += 1
                right += 1

            res = max(res, count)

        return res

        