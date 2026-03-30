class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(n)}

        for src, dst in edges:
            adj[src].append(dst)

        visited = set()
        visiting = set()
        res = []

        def dfs(cur):
            if cur in visited:
                return True
            if cur in visiting:
                return False

            visiting.add(cur)

            for neighbor in adj[cur]:
                if neighbor in visited:
                    continue
                if neighbor in visiting:
                    return False
                if not dfs(neighbor):
                    return False

            visited.add(cur)
            res.append(cur)
            visiting.remove(cur)

            return True

        for i in range(n):
            if not dfs(i):
                return []

        res.reverse()
        return res
                
                


