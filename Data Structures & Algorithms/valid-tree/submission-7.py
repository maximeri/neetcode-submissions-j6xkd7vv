class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for src, dst in edges:
            adj[src].append(dst)

        passed = set()

        def hasCycle(v, visited):
            if v in visited:
                return True

            visited.add(v)

            for nei in adj[v]:
                if hasCycle(nei, visited):
                    return True
            # broken tree
            if 0 not in visited:
                return True

            if v != 0:
                passed.add(v)
            
            return False

        for i in range(n):
            if i not in passed and hasCycle(i, set()):
                return False

        return True

