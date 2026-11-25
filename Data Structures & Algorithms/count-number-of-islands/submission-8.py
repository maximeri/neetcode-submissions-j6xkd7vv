class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set() # (r, c)
        count = 0

        def dfs(r, c):
            # if false return
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == "0":
                return

            # if true mark visited
            visited.add((r, c))

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1

        return count

            