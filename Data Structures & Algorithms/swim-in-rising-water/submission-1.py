class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        length = len(grid)
        minHeap = [(grid[0][0], 0, 0)] # w, r, c
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            max_t, curR, curC = heapq.heappop(minHeap)
            if curR < 0 or curC < 0 or curR == length or curC == length or (curR, curC) in visited:
                continue
            if curR == length - 1 and curC == length - 1:
                return max_t

            visited.add((curR, curC))

            for dr, dc in directions:
                neiR, neiC = curR + dr, curC + dc
                if neiR < 0 or neiC < 0 or neiR == length or neiC == length or (neiR, neiC) in visited:
                    continue
                heapq.heappush(minHeap, (max(grid[neiR][neiC], max_t), neiR, neiC))
            
                        
