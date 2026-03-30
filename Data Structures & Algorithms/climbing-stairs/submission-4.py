class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(i):
            if i >= n:
                return i == n # 在 Python 裡，True == 1，False == 0，所以這個 DFS 其實是在「用 boolean 當數字加」
            return dfs(i+1) + dfs(i+2)

        return dfs(0)