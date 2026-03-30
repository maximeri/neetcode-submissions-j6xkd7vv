class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # time MxN
        # space MxN
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()

        def dfs(r, c, visited):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == "0":
                return False
            visited.add((r,c))

            dfs(r-1, c, visited)
            dfs(r, c-1, visited)
            dfs(r+1, c, visited)
            dfs(r, c+1, visited)

            return True


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    if dfs(r, c, visited):
                        count += 1

        return count



                    