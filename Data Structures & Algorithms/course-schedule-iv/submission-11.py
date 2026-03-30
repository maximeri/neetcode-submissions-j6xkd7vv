class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        cache = [[-1] * numCourses for _ in range(numCourses)]

        for src, dst in prerequisites:
            adj[src].append(dst)
            cache[src][dst] = True

        def dfs(src, dst):
            if cache[src][dst] != -1:
                return cache[src][dst]

            for neighbor in adj[src]:
                if dfs(neighbor, dst):
                    cache[neighbor][dst] = True
                    return True

            cache[src][dst] = False    
            return False

        res = []
        for course, pre in queries:
            res.append(dfs(course, pre))

        return res

