class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for src, dst in edges:
            adj[src].append(dst)

        passed = set()

        def isValidTree(v, visited):
            # has cycle
            if v in visited:
                return False

            visited.add(v)

            for nei in adj[v]:
                if not isValidTree(nei, visited):
                    return False

            # broken tree
            if 0 not in visited:
                return False

            if v != 0:
                passed.add(v)
            
            return True

        for i in range(n):
            if i not in passed and not isValidTree(i, set()):
                return False

        return True

