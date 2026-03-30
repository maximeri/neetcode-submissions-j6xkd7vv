class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, visit, islands = len(grid), len(grid[0]), set(), 0

        # find the land and mark visited
        def dfs(r,c):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == "0":
                return

            visit.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1

        return islands

        
