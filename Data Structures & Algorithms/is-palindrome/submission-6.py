class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(char) -> bool:
            if ord("a") <= ord(char) <= ord("z"):
                return True

            if ord("A") <= ord(char) <= ord("Z"):
                return True

            if ord("0") <= ord(char) <= ord("9"):
                return True

            return False

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isAlphaNumeric(s[l]):
                l += 1
            while l < r and not isAlphaNumeric(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

        