class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        # init end count
        obstacleGrid[rows - 1][cols - 1] = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                # skip end
                if r == rows - 1 and c == cols - 1:
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                elif r == rows - 1:
                    obstacleGrid[r][c] = obstacleGrid[r][c + 1]
                elif c == cols - 1:
                    obstacleGrid[r][c] = obstacleGrid[r+1][c]
                else:
                    obstacleGrid[r][c] = obstacleGrid[r+1][c] + obstacleGrid[r][c+1]
        
        return obstacleGrid[0][0]
