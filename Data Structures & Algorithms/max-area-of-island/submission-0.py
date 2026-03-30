class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols, max_area, visit = len(grid), len(grid[0]), 0, set()

        # explore neighbor, mark visited, and count area
        def dfs(r,c):
            if r == rows or c == cols or min(r,c) < 0 or grid[r][c] == 0 or (r,c) in visit:
                return 0

            visit.add((r,c))

            area = 1

            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = dfs(r,c)
                    max_area = max(max_area, area)

        return max_area




