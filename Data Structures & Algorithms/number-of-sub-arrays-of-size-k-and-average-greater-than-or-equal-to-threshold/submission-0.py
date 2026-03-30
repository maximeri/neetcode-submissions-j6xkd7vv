class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        res = 0
        l = 0
        avg = 0
        for r in range(len(arr)):
            total += arr[r]
            if r - l + 1 > k:
                total -= arr[l]
                l += 1
                avg = 0
            if r - l + 1 == k and total / k  >= threshold:
                res += 1

        return res


            