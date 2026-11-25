class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set() # (r, c)
        rows, cols = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True

            if 0 <= r < rows and 0 <= c < cols and word[i] == board[r][c] and (r, c) not in visited:
                visited.add((r, c))
                found = dfs(r-1, c, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
                visited.remove((r, c))
                return found

            return False


        # find initial and dfs
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False

