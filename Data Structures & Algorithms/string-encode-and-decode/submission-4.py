class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            wPrefix = f"{len(s)}#{s}"
            result += wPrefix
        return result

    def decode(self, s: str) -> List[str]:
        # 10#MikeyChang2#Hi
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            stringLen = int(s[i:j])
            res.append(s[j + 1 : j + stringLen + 1])
            i = j + stringLen + 1
          
        return res


