class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)

        visited = set()
        visiting = set()
        topSort = []
        
        def dfs(src):
            if src in visiting:
                return False
            if src in visited:
                return True

            visiting.add(src)

            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
            
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)

            return True

        for i in range(n):
            if not dfs(i):
                return []

        topSort.reverse()
        return topSort


    



        
