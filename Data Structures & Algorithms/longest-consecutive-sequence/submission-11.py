class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxSeq = 0

        for num in nums:
            curSeq = 0
            curNum = num
            if curNum - 1 not in numsSet:
                while curNum in numsSet:
                    curSeq += 1
                    maxSeq = max(maxSeq, curSeq)
                    curNum += 1

        return maxSeq
        