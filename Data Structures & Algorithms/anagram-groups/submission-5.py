class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            label = "".join(sorted(s))
            result[label].append(s)

        return list(result.values())