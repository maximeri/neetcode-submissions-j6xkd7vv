class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        stack = [0]
        visited = set()
        visited.add(0)

        while stack:
            cur = stack.pop()
            for nei in adj[cur]:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)

        return len(visited) == n
            
