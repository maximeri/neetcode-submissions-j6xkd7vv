class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(x ** 2 + y ** 2, x, y) for x, y in points] # O(n)
        heapq.heapify(points) # O(n)

        res = []
        # O(k * log(n))
        while k > 0: 
            _, x, y = heapq.heappop(points) 
            res.append([x, y])
            k -= 1

        return res