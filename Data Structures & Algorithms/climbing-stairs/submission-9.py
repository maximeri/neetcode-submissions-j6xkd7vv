class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        cur, nxt = 2, 3
        
        for i in range(3, n):
            newNxt = cur + nxt
            cur = nxt
            nxt = newNxt

        return nxt

            
