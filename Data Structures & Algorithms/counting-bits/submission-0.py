class Solution:
    def countBits(self, n: int) -> List[int]:
        # bits[i] = bits[i >> 1] + (i & 1)
        bits = [0] * (n + 1) # starts from 0
        for i in range(n+1):
            bits[i] = bits[i >> 1] + (i & 1)

        return bits



