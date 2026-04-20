class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        # 如果我們只看 $s1$ 的前 $i$ 個字元，和 $s2$ 的前 $j$ 個字元，它們到底能不能交錯拼湊出 $s3$ 的前 $i+j$ 個字元？
        dp[0][0] = True

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                take_s1 = dp[i-1][j] and s1[i-1] == s3[i + j - 1]
                take_s2 = dp[i][j-1] and s2[j-1] == s3[i + j - 1]
                dp[i][j] = take_s1 or take_s2

        return dp[len(s1)][len(s2)]



        