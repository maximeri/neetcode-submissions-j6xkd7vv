class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            sLen = len(s)
            encoded += f"{sLen}#{s}"

        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + length + 1]
            res.append(word)
            i = j + length + 1

        return res


        




