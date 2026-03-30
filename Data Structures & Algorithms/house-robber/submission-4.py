class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] 從第 0..i 這些房子中，能偷到的最大金額
        rob1, rob2 = 0, 0
        for num in nums:
            maxAmount = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = maxAmount

        return rob2