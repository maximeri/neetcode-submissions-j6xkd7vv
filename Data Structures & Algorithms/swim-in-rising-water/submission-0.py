class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        minHeap = []
        heapq.heappush(minHeap, [grid[0][0], 0, 0])
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return t

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR == rows or neiC == cols or (neiR, neiC) in visited):
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minHeap, [max(grid[neiR][neiC], t), neiR, neiC])



        