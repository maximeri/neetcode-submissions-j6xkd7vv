class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 「把這堆石頭分成兩組，讓這兩組的重量越接近越好。」這就是為什麼我們不用 Heap，而是用 背包問題（0/1 Knapsack）。我們要找出一組石頭，其總和儘量接近「總重量的一半」。
        total = sum(stones)
        target = total // 2
        total_table = {}

        def findMaxPair(i, curSum):
            if (i, curSum) in total_table:
                return curSum

            if i == len(stones):
                return curSum

            total_table[(i, curSum)] = findMaxPair(i+1, curSum)

            # choose
            newSum = curSum + stones[i]
            if newSum <= target:
                total_table[(i, curSum)] = max(total_table[(i, curSum)], findMaxPair(i+1, newSum))

            return total_table[(i, curSum)]

        pair1 = findMaxPair(0, 0)
        pair2 = total - pair1

        return abs(pair1 - pair2)