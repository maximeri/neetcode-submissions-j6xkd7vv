class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        length = 0
        res = ""
        # odd
        for i in range(len(s)):
            l, r = i, i
            curWord = s[i]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curWord += s[l]
                if r - l + 1 > length:
                    res = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1
        # even
            l, r = i, i+1
            curWord = s[:i+2]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > length:
                    res = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1
                
        return res
        

        

        


