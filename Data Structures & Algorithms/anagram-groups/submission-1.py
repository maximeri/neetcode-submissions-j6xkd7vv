# Hsuan Hsuan
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solution
        # res = defaultdict(list)
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(s)

        # return list(res.values())

        # if the characters may be non-alphabetic
        res = defaultdict(list)
        for s in strs:
            count = defaultdict(int)
            for c in s:
                count[c] += 1
            res[tuple(sorted(count.items()))].append(s)
        
        return list(res.values())