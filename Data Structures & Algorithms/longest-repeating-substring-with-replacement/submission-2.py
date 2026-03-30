# Hsuan Hsuan
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initial thought:
        # keep a list of the position of replaced character
        # iterate throught the slice with sliding window
        # left stays until k characters are replaced
        # left moves to the left most position + 1 of the replaced character
        # above is too naive, there may be multiple characters and which one should we be replacing

        # solution
        count = defaultdict(int)
        res = 0
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(count[s[r]], maxFreq)
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1 
            res = max(res, r - l + 1)
        return res

