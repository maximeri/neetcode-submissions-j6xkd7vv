class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in bracket_map:
                stack.append(char)
            elif char in bracket_map.values():
                if not stack:
                    return False
                if char != bracket_map[stack.pop()]:
                    return False

        return not stack