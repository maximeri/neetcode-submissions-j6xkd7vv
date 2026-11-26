class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)] # 0:[1, 2] 1: [0]
        for src, dst in prerequisites:
            adjList[src].append(dst)

        checked = set()

        # has cycle
        def hasCycle(course, visited):
            if course in visited:
                return True

            if course in checked:
                return False

            visited.add(course)
            for pre in adjList[course]:
                if hasCycle(pre, visited):
                    return True

            checked.add(course)
            visited.remove(course)

            return False

        for i in range(numCourses):
            if hasCycle(i, set()):
                return False

        return True


        