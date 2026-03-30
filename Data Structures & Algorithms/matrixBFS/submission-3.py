class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        q.append((0,0))
        visit = set()
        visit.add((0,0))
        length = 0

        while q: 
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length

                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visit:
                        visit.add((nr, nc))
                        q.append((nr, nc))
                
            length += 1

        return -1
                



                