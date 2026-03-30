class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0))
        visit = set()
        visit.add((0, 0))
        length = 1

        if grid[0][0] or grid[rows - 1][cols - 1]:
            return -1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # reached exit
                if r == rows - 1 and c == cols - 1:
                    return length

                # 8 directions (including diagonals)
                directions = [
                    (1, 0), (-1, 0), (0, 1), (0, -1),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)
                ]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc, 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr,nc) not in visit:
                        visit.add((nr, nc))
                        queue.append((nr,nc))
            length += 1

        return - 1



