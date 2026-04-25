class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = defaultdict(int)
        for i in range(len(s)):
            char_count[s[i]] += 1
            char_count[t[i]] -= 1

        for val in char_count.values():
            if val != 0:
                return False

        return True
