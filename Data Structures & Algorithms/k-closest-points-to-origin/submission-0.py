class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(x ** 2 + y ** 2, x, y) for x, y in points]
        heapq.heapify(points)


        res = []
        while k > 0:
            _, x, y = heapq.heappop(points)
            res.append([x, y])
            k -= 1

        return res