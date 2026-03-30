class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        isPre = [[-1] * numCourses for _ in range(numCourses)]

        for src, dst in prerequisites:
            adj[src].append(dst)
            isPre[src][dst] = True

        

        def dfs(src, dst):
            if isPre[src][dst] != -1:
                return isPre[src][dst] == 1

            for neighbor in adj[src]:
                if neighbor == src or dfs(neighbor, dst):
                    isPre[src][dst] = 1
                    return True

            isPre[src][dst] = 0
            return False

        res = []
        for src, dst in queries:
            res.append(dfs(src, dst))

        return res

