class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            label = [0] * 26
            for c in s:
                label[ord(c) - ord('a')] += 1
            res[tuple(label)].append(s)

        return list(res.values())