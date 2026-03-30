class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque() # 先塞起始座標
        queue.append((0,0))
        visit.add((0,0)) # 先塞起始座標

        steps = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                
                # exit found!
                if r == rows - 1 and c == cols -1:
                    return steps

                nr = r+1
                nc = c
                if  0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visit and grid[nr][nc] == 0:
                    visit.add((nr,nc))
                    queue.append((nr,nc))

                nr = r-1
                nc = c
                if  0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visit and grid[nr][nc] == 0:
                    visit.add((nr,nc))
                    queue.append((nr,nc))

                nr = r
                nc = c+1
                if  0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visit and grid[nr][nc] == 0:
                    visit.add((nr,nc))
                    queue.append((nr,nc))

                nr = r
                nc = c-1
                if  0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visit and grid[nr][nc] == 0:
                    visit.add((nr,nc))
                    queue.append((nr,nc))

            steps += 1

        # no such path
        return -1




