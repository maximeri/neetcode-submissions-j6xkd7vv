class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            wPrefix = f"{len(s)}#{s}"
            res += wPrefix
        return res
        
    def decode(self, s: str) -> List[str]:
        # 10#Oragnegeer2#OK

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            res.append(s[j : j + length])
            i = j + length

        return res

