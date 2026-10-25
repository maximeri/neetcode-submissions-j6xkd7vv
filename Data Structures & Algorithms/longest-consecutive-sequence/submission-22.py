class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                curNum = num
                curLen = 0
                while curNum in numSet:
                    curLen += 1
                    curNum += 1

                longest = max(longest, curLen)

        return longest