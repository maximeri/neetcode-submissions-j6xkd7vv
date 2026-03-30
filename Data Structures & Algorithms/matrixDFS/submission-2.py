class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])


        def dfs(r,c,visit):
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == 1 or (r,c) in visit:
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1

            path = 0
            visit.add((r,c))

            path += dfs(r+1, c, visit)
            path += dfs(r-1, c, visit)
            path += dfs(r, c+1, visit)
            path += dfs(r, c-1, visit)

            visit.remove((r,c))

            return path


        return dfs(0,0,set())
