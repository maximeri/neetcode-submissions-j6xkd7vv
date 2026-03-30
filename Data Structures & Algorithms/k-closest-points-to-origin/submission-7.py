class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points: # O(n)
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(heap, [dist, x, y]) 
            # heap 永遠不會超過 k + 1 個元素
            # 一超過 k，你立刻 pop 掉一個
            if len(heap) > k: 
                heapq.heappop(heap) # O(logk)
        
       
        res = []
        while heap:
            _, x, y = heapq.heappop(heap)
            res.append([x,y])

        return res
