class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for src, dst in prerequisites:
            adj[src].append(dst)

        visiting = set()
        visited = set()
        res = []

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
            res.append(src)

            return True

        for i in range(numCourses):
            if not topSort(i):
                return []

        return res