class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1, prev2 = 1, 2

        for i in range(3, n+1):
            tmpPrev1 = prev1
            prev1 = prev2
            prev2 = tmpPrev1 + prev2

        return prev2
