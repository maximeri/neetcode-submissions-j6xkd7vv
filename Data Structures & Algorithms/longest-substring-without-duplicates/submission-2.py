# Hsuan Hsuan review
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mp and mp[s[r]] >= l:
                l = mp[s[r]] + 1
            if l > r:
                break
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

            