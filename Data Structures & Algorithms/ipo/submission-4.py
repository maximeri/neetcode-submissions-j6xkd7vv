class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        available_profits = []
        curProjectIdx = 0
        n = len(projects)
        res = 0

        for _ in range(k):
            while curProjectIdx < n and w >= projects[curProjectIdx][0]:
                heapq.heappush(available_profits, -projects[curProjectIdx][1])
                curProjectIdx += 1

            if available_profits:
                w += -heapq.heappop(available_profits)
            else:
                break

        return w
