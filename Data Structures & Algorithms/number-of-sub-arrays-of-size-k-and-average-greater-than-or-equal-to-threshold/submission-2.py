class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k 
        curSum = 0
        res = 0

        for r in range(len(arr)):
            curSum += arr[r]
            if r >= k - 1:
                res += curSum >= threshold
                curSum -= arr[r-k+1]

        return res


        