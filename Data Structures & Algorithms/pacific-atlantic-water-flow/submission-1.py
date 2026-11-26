class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])

        # store (r, c) in pac, atl
        # record cells that ocean can reach
        # false: out of bounds, visited, too high
        def recordCells(r, c, cells, prevHeight):
            if (r, c) in cells or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight:
                return
            cells.add((r, c))
            recordCells(r-1, c, cells, heights[r][c])
            recordCells(r+1, c, cells, heights[r][c])
            recordCells(r, c-1, cells, heights[r][c])
            recordCells(r, c+1, cells, heights[r][c])

        # traverse col p
        for i in range(cols):
            recordCells(0, i, pac, heights[0][i])
            recordCells(rows - 1, i, atl,heights[rows-1][i])

        # traverse row p
        for i in range(rows):
            recordCells(i, 0, pac, heights[i][0])
            recordCells(i, cols - 1, atl, heights[i][cols-1])

        res = pac.intersection(atl)
        # {(0,0), (0,1)} => [[0,0],[0,1]]
        converted = [list(t) for t in res]
        # converted = []
        # for t in res:
        #     converted.append(list(t))

        return converted


        

