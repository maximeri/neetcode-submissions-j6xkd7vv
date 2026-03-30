class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        targetSum = threshold * k
        res = curSum = 0
        for r in range(len(arr)):
            curSum += arr[r]
            if r >= k - 1:
                res += curSum >= targetSum
                curSum -= arr[r - k + 1]

        return res


            