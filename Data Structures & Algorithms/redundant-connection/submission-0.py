class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n = edge count + 1 because the quiz said there's one cycle 
        n = len(edges) + 1
        parent = [i for i in range(n)]
        rank = [1] * n

        # find root and make everyone root the same(compress)
        def find(n):
            if n == parent[n]:
                return n
            parent[n] = find(parent[n])
            return parent[n]

        # merge components
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1 == r2:
                return False # 合併失敗
            if rank[r1] > rank[r2]:
                parent[r2] = r1
            if rank[r1] < rank[r2]:
                parent[r1] = r2
            if rank[r1] == rank[r2]:
                parent[r1] = r2
                rank[r1] += 1
            return True # 成功合併
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            


