class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(steps):
            if steps >= n:
                return steps == n
            if steps in cache:
                return cache[steps]
            cache[steps] = dfs(steps + 1) + dfs(steps + 2)
            return cache[steps]

        return dfs(0)