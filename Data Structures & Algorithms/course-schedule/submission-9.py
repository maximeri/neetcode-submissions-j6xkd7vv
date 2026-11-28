class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)] # 0: [1, 2]
        checked = set()

        for src, dst in prerequisites:
            adjList[src].append(dst)

        def hasCycle(vertex, visited):
            if vertex in checked:
                return False
                
            if vertex in visited:
                return True

            visited.add(vertex)

            for nei in adjList[vertex]:
                if hasCycle(nei, visited):
                    return True

            checked.add(vertex)
            visited.remove(vertex)

            return False


        for i in range(numCourses):
            if hasCycle(i, set()):
                return False

        return True