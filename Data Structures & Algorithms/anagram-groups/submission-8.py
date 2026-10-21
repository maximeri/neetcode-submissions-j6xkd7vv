class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        # "act" : [1,2,3]
        for s in strs:
            label = [0] * 26
            for char in s:
                label[ord(char) - ord("a")] += 1
            result[tuple(label)].append(s)
        
        return list(result.values())