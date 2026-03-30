class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, 0)] # distance, points index
        visited, res = set(), 0

        while minHeap:
            curW, curI = heapq.heappop(minHeap)
            if curI in visited:
                continue
                
            visited.add(curI)
            res += curW
            for neiI, p in enumerate(points):
                dist = abs(points[curI][0] - points[neiI][0]) + abs(points[curI][1] - points[neiI][1])
                heapq.heappush(minHeap, (dist, neiI))

        return res