class Solution:
    def rob(self, nums: List[int]) -> int:
        pre, cur = 0, 0  # rob1=dp[i-2], rob2=dp[i-1]
        for num in nums:
            newCur = max(pre + num, cur)
            pre = cur
            cur = newCur
            
        return cur


            