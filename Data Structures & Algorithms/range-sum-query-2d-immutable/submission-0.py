class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.p = [[0] * (cols+1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                # Padding 座標 (r+1, c+1)
                # 公式: 上 + 左 - 左上 + 自己
                self.p[r+1][c+1] = self.p[r][c+1] + self.p[r+1][c] - self.p[r][c] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 大矩形 - 上半部 - 左半部 + 左上角(加回)
        return self.p[row2+1][col2+1] - self.p[row1][col2+1] - self.p[row2+1][col1] + self.p[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)