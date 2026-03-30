class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            return True
        return False
    

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for u, v, w in edges:
            heapq.heappush(minHeap, [w, u, v])

        unionFind = UnionFind(n)
        res, components = 0, n

        while components > 1 and minHeap:
            w, u, v = heapq.heappop(minHeap)
            if unionFind.union(u, v):
                res += w
                components -= 1

        return res if components == 1 else -1
