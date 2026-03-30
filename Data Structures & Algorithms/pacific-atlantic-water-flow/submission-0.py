class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c, visit, preHeight):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit or heights[r][c] < preHeight:
                return
            visit.add((r,c))
            preHeight = heights[r][c]
            dfs(r+1,c, visit, preHeight)
            dfs(r-1,c, visit, preHeight)
            dfs(r,c+1, visit, preHeight)
            dfs(r,c-1, visit, preHeight)


        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols -1,atl,heights[r][cols -1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res

