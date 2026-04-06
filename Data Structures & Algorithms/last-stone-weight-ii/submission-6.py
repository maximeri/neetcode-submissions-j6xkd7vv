class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = stone_sum // 2
        memo = {}

        def dfs(i, cur_sum):
            if i == len(stones):
                return abs(stone_sum - 2 * cur_sum)

            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            memo[(i, cur_sum)] = min(dfs(i+1, cur_sum), dfs(i+1, cur_sum + stones[i]))

            return memo[(i, cur_sum)]

        return dfs(0, 0)



            

            