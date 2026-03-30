class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # n = 1010
        # n - 1 = 1010 - 1 = 1001 
        # 1010 & 1001 =  1000
        # n - 1 = 1000 - 1 = 111
        # 1000 & 111 =  0000
        # res = 2

        while n:
            n &= n - 1
            res += 1
        return res

