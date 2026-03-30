class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arrSumMap = {0: 1}
        prefixSum = 0
        ans = 0

        for num in nums:
            prefixSum += num

            # ① 先用「過去的 prefix sum」算答案
            ans += arrSumMap.get(prefixSum - k, 0)

            # ② 再把現在的 prefix sum 記進去
            arrSumMap[prefixSum] = arrSumMap.get(prefixSum, 0) + 1

        return ans
