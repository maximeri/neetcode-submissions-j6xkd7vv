# hsuan hsuan
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initial thought:
        # iterate once, skip if non-alphanumeric
        # check is same until two pointer cross each other
    

        # after reading solution
        # no need to treat even/odd character count differently
        # while l < r and check condition: l++
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while r > l and not self.isAlphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True


    def isAlphaNumeric(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
        ord('A') <= ord(c) <= ord('Z') or
        ord('0') <= ord(c) <= ord('9'))


# python libs: ord('') , .lower()
