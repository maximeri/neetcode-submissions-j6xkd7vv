class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set()
        count = 0

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def markVisited(v):
            if v in visited:
                return

            visited.add(v)

            for nei in adj[v]:
                markVisited(nei)

            return

        for i in range(n):
            if i not in visited:
                count += 1
                markVisited(i)


        return count