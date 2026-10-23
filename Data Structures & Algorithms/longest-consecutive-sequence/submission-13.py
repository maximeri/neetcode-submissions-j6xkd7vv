class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLen = 0

        for i in range(len(nums)):
            curLen = 1
            curNum = nums[i]
            if curNum - 1 not in numsSet:
                while curNum + 1 in numsSet:
                    curLen += 1
                    curNum += 1

            maxLen = max(maxLen, curLen)

        return maxLen