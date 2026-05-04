class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # 1. 建立目標頻率表 (s1)
        target_counts = {}
        for char in s1:
            target_counts[char] = target_counts.get(char, 0) + 1

        # 2. 建立當前窗口頻率表 (s2 的前 n1 個字元)
        window_counts = {}
        for i in range(n1):
            char = s2[i]
            window_counts[char] = window_counts.get(char, 0) + 1

        if target_counts == window_counts:
            return True

        for i in range(n1, n2):
            in_char = s2[i]
            out_char = s2[i - n1]

            window_counts[in_char] = window_counts.get(in_char, 0) + 1
            window_counts[out_char] -= 1

            if window_counts[out_char] == 0:
                del window_counts[out_char]

            if target_counts == window_counts:
                return True

        return False





        
