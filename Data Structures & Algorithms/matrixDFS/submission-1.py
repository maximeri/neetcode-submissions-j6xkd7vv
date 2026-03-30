class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(grid,r,c,visit):
            if r == rows or c == cols or min(r,c) < 0 or grid[r][c] == 1 or (r,c) in visit:
                return 0

            if r == rows - 1 and c == cols -1:
                return 1

            visit.add((r,c))

            path = 0
            path += dfs(grid, r+1, c, visit)
            path += dfs(grid, r-1, c, visit)
            path += dfs(grid, r, c+1, visit)
            path += dfs(grid, r, c-1, visit)

            visit.remove((r,c))

            return path

        return dfs(grid, 0, 0, set())



        