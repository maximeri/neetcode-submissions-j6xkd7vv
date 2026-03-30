class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minHeap = [(0, 0)]
        res = 0

        while minHeap and len(visited) < len(points):
            curW, curI  = heapq.heappop(minHeap)
            if curI in visited:
                continue
            visited.add(curI)
            res += curW

            for neiI in range(len(points)):
                if neiI not in visited:
                    manhat_dist = abs(points[neiI][0] - points[curI][0]) + abs(points[neiI][1] - points[curI][1])
                    heapq.heappush(minHeap, (manhat_dist, neiI))

        return res
