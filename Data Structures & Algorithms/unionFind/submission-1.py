class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.num_components = n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[px] += 1
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components
