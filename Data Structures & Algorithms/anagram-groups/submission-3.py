class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        def get_profile(string):
            count = [0] * 26
            for char in string:
               count[ord(char) - ord("a")] += 1
            return tuple(count)
                

        for s in strs:
            count = get_profile(s)
            res[count].append(s)


        return list(res.values())
