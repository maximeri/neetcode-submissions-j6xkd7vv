class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        if len(s1) > len(s2):
            s1, s2 = s2, s1

        dp = [False] * (len(s1)+1)
        dp[0] = True

        for i in range(1, len(s1) + 1):
            dp[i] = dp[i-1] and s1[i-1] == s3[i-1]

        for j in range(1, len(s2) + 1):
            # 左上
            dp[0] = dp[0] and s2[j-1] == s3[j-1]
            for i in range(1, len(s1) + 1):
                # 左
                take_s1 = dp[i-1] and s1[i-1] == s3[i + j - 1]
                # dp[i] 還沒被更新，所以是上面
                take_s2 = dp[i] and s2[j-1] == s3[i + j - 1]
                dp[i] = take_s1 or take_s2


        return dp[len(s1)]



        