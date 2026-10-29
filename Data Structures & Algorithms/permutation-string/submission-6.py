class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target_counts = defaultdict(int)

        for char in s1:
            target_counts[char] += 1

        window_counts = defaultdict(int)

        l = 0
        for r in range(len(s2)):
            window_counts[s2[r]] += 1

            if (r - l + 1) > len(s1):
                if window_counts[s2[l]] > 1:
                    window_counts[s2[l]] -= 1
                else:
                    window_counts.pop(s2[l])
                l += 1

            if window_counts == target_counts:
                return True

        return False

            

            
