class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for src, dst in prerequisites:
            adj[src].append(dst)

        visiting = set()
        visited = set()

        def topSort(src):
            if src in visiting:
                return False
            if src in visited:
                return True

            visiting.add(src)

            for neighbor in adj[src]:
                if neighbor in visiting:
                    return False
                topSort(neighbor)

            visiting.remove(src)
            visited.add(src)

            return True

        for i in range(numCourses):
            if not topSort(i):
                return False

        return True
            
            