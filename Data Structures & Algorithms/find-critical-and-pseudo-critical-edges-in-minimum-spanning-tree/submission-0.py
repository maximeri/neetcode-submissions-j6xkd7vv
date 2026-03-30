class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
           e.append(i) # u, v, w, i

        edges.sort(key=lambda x: x[2])

        mst_w = 0
        uf = UnionFind(n)

        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_w += w

        critical, pseudo = [], []

        for n1, n2, nw, i in edges:
            uf = UnionFind(n)
            temp_weight = 0
            connected_count = 0
            # remove cur edge to test if it's critical
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    temp_weight += w
                    connected_count += 1
            # 如果連不通 (edges < n-1) 或者 總權重變大，它就是關鍵邊
            if connected_count < n - 1 or temp_weight > mst_w:
                critical.append(i)
                continue

            # 如果強制使用後，總權重依然等於最小權重，且能連通所有點 it's psuedo critical
            temp_weight_force = nw # 先把這條邊的權重算進去
            uf = UnionFind(n)
            uf.union(n1, n2)     # 強制連通這條邊
            connected_count = 1
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    temp_weight_force += w
                    connected_count += 1
            if connected_count == n - 1 and temp_weight_force == mst_w:
                pseudo.append(i)
        return [critical, pseudo]
        

        