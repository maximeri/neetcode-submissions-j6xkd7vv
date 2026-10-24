class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        labels = defaultdict(list)
        for s in strs:
            label = [0] * 26
            for char in s:
                label[ord(char) - ord("a")] += 1
            labels[tuple(label)].append(s)
        return list(labels.values())