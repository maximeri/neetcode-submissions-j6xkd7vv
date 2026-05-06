class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        target, window = [0] * 26, [0] * 26
        aOrder = ord("a")
        for i in range(len(s1)):
            target[ord(s1[i]) - aOrder] += 1
            window[ord(s2[i]) - aOrder] += 1

        if window == target:
            return True

        for i in range(n1, n2):
            window[ord(s2[i]) - aOrder] += 1
            window[ord(s2[i-n1]) - aOrder] -= 1

            if window == target:
                return True

        return False

