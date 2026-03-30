class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        max_count = 0
        for n in hset:
            if n - 1 not in hset:
                count, curNum = 1, n
                while curNum + 1 in hset:
                    curNum += 1
                    count += 1
                max_count = max(max_count, count)

        return max_count