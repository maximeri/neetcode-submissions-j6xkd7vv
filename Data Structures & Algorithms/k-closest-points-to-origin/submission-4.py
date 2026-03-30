class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(-(x**2 + y**2),x,y) for x,y in points]
        heapq.heapify(points)
       
        while len(points) - k > 0:
            heapq.heappop(points)
        res = []
        while points:
            _, x, y = heapq.heappop(points)
            res.append([x,y])

        return res
