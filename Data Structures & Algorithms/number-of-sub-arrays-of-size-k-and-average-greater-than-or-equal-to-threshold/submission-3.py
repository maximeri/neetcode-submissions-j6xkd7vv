class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k 
        curSum = 0
        res = 0

        for r in range(len(arr)):
            curSum += arr[r]
            if r >= k - 1: # 當索引 r 到達 k-1，代表窗口已滿，開始判斷並移動窗口
                res += curSum >= threshold
                curSum -= arr[r-k+1]

        return res


        