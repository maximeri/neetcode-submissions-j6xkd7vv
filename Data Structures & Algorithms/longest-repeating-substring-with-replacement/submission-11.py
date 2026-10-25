class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFrq = defaultdict(int)
        globalMax, windowMax = 0, 0
        l = 0

        for r in range(len(s)):
            charFrq[s[r]] += 1
            windowMax = max(charFrq[s[r]], windowMax)
            while windowMax + k < r - l + 1:
                charFrq[s[l]] -= 1
                l += 1
            globalMax = max(globalMax, r - l + 1)

        return globalMax
