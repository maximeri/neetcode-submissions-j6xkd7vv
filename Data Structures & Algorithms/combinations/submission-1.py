class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb, curComb = [], []

        def helper(i, comb, curComb, n, k):
            if len(curComb) == k:
                comb.append(curComb.copy())
                return

            if i > n:
                return

            for j in range(i, n+1):
                curComb.append(j)
                helper(j+1, comb, curComb, n, k)
                curComb.pop()
        
        helper(1, comb, curComb, n, k)

        return comb