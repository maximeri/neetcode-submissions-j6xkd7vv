
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        # -6 -4 -3 -2 -2
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, first - second)

        return abs(stones[0]) if stones else 0
