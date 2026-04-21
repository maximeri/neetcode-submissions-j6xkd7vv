class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        m, n = len(str1), len(str2)

        dp = [""] * (n + 1)

        for j in range(1, n + 1):
            dp[j] = str2[:j]


        for i in range(1, m + 1):
            up_left = dp[0]
            dp[0] = str1[:i]
            for j in range(1, n + 1):
                next_up_left = dp[j]
                if str1[i-1] == str2[j-1]:
                    dp[j] = up_left + str1[i-1]
                else:
                    pick_from_above = dp[j] + str1[i-1]
                    pick_from_left = dp[j-1] + str2[j-1]
                    if len(pick_from_above) < len(pick_from_left):
                        dp[j] = pick_from_above
                    else:
                        dp[j] = pick_from_left
                up_left = next_up_left

        return dp[n]
