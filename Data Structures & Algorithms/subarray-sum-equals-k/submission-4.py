class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前綴和 (Prefix Sum)： 永遠是從起點 arr[0] 開始加總的片段。
        # 子陣列 (Subarray)： 可以是陣列中任意一段連續的片段（不一定包含 arr[0]）。
        # current sum = 從陣列的第一個元素 當前累積和 （是現在從頭加到尾的總和）
        # previous sum = 是過去從頭加到某處的總和
        # current sum - previous sum = 中間夾住的子陣列總和 k
        # current sum - k = previous sum

        curSum = 0
        sumFreq = {0:1} # 總和為 0 的前綴和，在最一開始已經出現過 1 次
        count = 0
        for num in nums:
            curSum += num
            if curSum - k in sumFreq:
                count += sumFreq[curSum - k]
            sumFreq[curSum] = sumFreq.get(curSum, 0) + 1

        return count

            
