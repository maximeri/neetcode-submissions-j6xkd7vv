# Hsuan Hsuan
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # solution:
        # hard: how to not look back
        # approach 1:  delete from set
        chars = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(r - l + 1, res)
        return res

        # approach 2: compare the current postion first so that we will not jump back



