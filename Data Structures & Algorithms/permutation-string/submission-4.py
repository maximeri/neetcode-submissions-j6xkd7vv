class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_char = defaultdict(int)
        for char in s1:
            s1_char[char] += 1

        # a: 1, b: 1, c: 1



        for l in range(len(s2)):
            cur_char = s1_char.copy()
            if s2[l] in s1_char:
                r = l
                while r < len(s2) and r - l < len(s1):
                    cur_char[s2[r]] -= 1
                    r += 1

                if all(count == 0 for count in cur_char.values()):
                    return True

        return False


