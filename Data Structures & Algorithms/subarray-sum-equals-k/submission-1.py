class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arrSumMap = {0:1}
        prefixSum = 0
        ans = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in arrSumMap:
                ans += arrSumMap[prefixSum - k]
            arrSumMap[prefixSum] = arrSumMap.get(prefixSum, 0) + 1
        
        return ans
