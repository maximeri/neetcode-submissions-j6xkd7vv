import heapq

class MedianFinder:
    def __init__(self):
        # small: Max-Heap，儲存較小的一半數字 (為了用 Python 的 min-heap 模擬，存入時要取負號)
        # large: Min-Heap，儲存較大的一半數字
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # 1. 預設先丟進 small (Max-Heap)
        #    注意：Python heapq 預設是 min-heap，所以存入 small 要用 -num
        heapq.heappush(self.small, -num)

        # 2. 為了平衡，將 small 的最大值彈出並塞進 large
        #    這保證了 small 裡面的所有數都小於等於 large 裡面的數
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # 3. 檢查數量平衡：如果 large 的數量比 small 多超過 1 個
        #    (或者你可以約定 small 的數量永遠大於等於 large)
        #    將 large 的最小值彈回 small，確保兩邊數量差不超過 1
        if len(self.large) - len(self.small) > 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:
        # 1. 如果兩邊數量相等：
        #    中位數就是 (small 的最大值 + large 的最小值) / 2
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        
        # 2. 如果數量不相等：
        #    看哪邊人多，中位數就是人多的那個堆積的頂端元素
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]

        