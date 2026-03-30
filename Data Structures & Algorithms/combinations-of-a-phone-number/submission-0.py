class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtracking(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for char in digitToChar[digits[i]]:
                backtracking(i + 1, curStr + char)

        if digits:
            backtracking(0, "")

        return res


            
            

        