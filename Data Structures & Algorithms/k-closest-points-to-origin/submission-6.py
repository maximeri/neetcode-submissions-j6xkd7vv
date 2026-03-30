class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points: # O(n)
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(heap, [dist, x, y]) # O(logn)
            if len(heap) > k: # O(logk)
                heapq.heappop(heap)
        
       
        res = []
        while heap:
            _, x, y = heapq.heappop(heap)
            res.append([x,y])

        return res
