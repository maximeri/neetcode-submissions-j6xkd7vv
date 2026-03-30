class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        bot, top = 0, rows - 1

        while bot <= top:
            row = (top + bot) // 2
            if target > matrix[row][cols - 1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                break
        
        bot, top = 0, cols - 1

        while bot <= top:
            col = (top + bot) // 2
            if target < matrix[row][col]:
                top = col - 1
            elif target > matrix[row][col]:
                bot = col + 1
            else:
                return True
        return False


