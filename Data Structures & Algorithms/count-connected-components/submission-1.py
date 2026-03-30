class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        count = n

        def find(i):
            if i == parents[i]:
                return i
            parents[i] = find(parents[i])
            return parents[i]

        def union(i, j):
            nonlocal count
            r1, r2 = find(i), find(j)
            if r1 != r2:
                parents[r1] = r2
                count -= 1

        for i, j in edges:
            union(i, j)
        
        return count

        

        
