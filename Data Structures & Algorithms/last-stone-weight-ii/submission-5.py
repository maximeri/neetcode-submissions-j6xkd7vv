class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        # r: the i's stone c: cur target, [r][c] = max target value
        maxTarget = [[0] * (target + 1) for _ in range(len(stones) + 1)]

        for i in range(1, len(stones) + 1):
            for t in range(target + 1):
                maxTarget[i][t] = maxTarget[i-1][t]
                if stones[i-1] <= t:
                    maxTarget[i][t] = max(maxTarget[i][t], maxTarget[i-1][t-stones[i-1]] + stones[i-1])

        pair1 = maxTarget[len(stones)][target]
        pair2 = total - pair1
        return abs(pair1 - pair2)


