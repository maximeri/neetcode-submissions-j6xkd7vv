class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check box
        # i: 4  4  4   4  4  4   4  4  4 哪盒

        # j: 0  1  2   3  4  5   6  7  8 哪個

        # 00 01 02  
        # 10 11 12
        # 20 21 22

        # 30 31 32  33 34 35
        # 40 41 42  43 44 45
        # 50 51 52  53 54 55

        # (i // 3) * 3 + (j // 3)
        # 
       
        for i in range(9):
            cur_nums_row = set()
            cur_nums_column = set()
            cur_nums_box = set()

            for j in range(9):
                # check row
                if board[i][j] in cur_nums_row:
                    return False

                if board[i][j] != ".":
                    cur_nums_row.add(board[i][j])

                # check column
                if board[j][i] in cur_nums_column:
                    return False

                if board[j][i] != ".":
                    cur_nums_column.add(board[j][i])

                # # check box
                r = (i // 3) * 3 + j // 3
                c = (i % 3) * 3 +  j % 3
                val = board[r][c]

                if val in cur_nums_box:
                    return False

                if val != ".":
                    cur_nums_box.add(val)

        return True

