class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, visit, count = len(grid), len(grid[0]), set(), 0

        # explore neighbors and mark visited
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if grid[r][c] == "0" or (r, c) in visit:
                return
            # if not visited mark visited
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # traverse grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    count += 1

        return count
