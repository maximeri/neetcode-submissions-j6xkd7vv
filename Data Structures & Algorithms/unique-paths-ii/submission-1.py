class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0
        # dp[r][c] = dp[r-1][c] + dp[r][c-1]
        obstacleGrid[0][0] = 1
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                elif r == 0:
                    obstacleGrid[r][c] = obstacleGrid[r][c-1]
                elif c == 0:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c]
                else:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]

        return obstacleGrid[rows-1][cols-1]

