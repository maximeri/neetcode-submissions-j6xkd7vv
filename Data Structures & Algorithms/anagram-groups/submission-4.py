class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            sortedstr = "".join(sorted(s))
            result[sortedstr].append(s)

            
        return list(result.values())

