class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}" : "{", "]" : "[", ")":"("}
        for c in s:
            if c in closeToOpen:
                if not stack:           
                    return False
                if stack.pop()!= closeToOpen[c]:
                    return False
            else:
                stack.append(c)
                
        return not stack
            

