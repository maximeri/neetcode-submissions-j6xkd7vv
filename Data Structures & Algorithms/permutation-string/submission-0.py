class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1, count_s2 = {}, {}
        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1

        need, have = len(count_s1), 0
        for l in range(len(s2)):
            count_s2, have = {}, 0
            for r in range(l, len(s2)):
                char = s2[r]
                if char not in count_s1:
                    break
                count_s2[char] = count_s2.get(char, 0) + 1

                if count_s2[char] == count_s1[char]:
                    have += 1

                if need == have:
                    return True

                if count_s2[char] > count_s1[char]:
                    break

                if r - l + 1 > len(s1):
                    break

        return False
