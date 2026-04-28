class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            data = str(len(string)) + "#" + string
            res += data

        return res
        # 3#cat4#book
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            word = s[i:j]
            res.append(word)
            i = j

        return res

