# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validateBST(node, lowBound, upBound):
            if not node:
                return True

            if not (lowBound < node.val < upBound):
                return False

            validateLeft = True
            validateRight = True

            if node.left:
                validateLeft = validateBST(node.left, lowBound, node.val)

            if node.right:
                validateRight = validateBST(node.right, node.val, upBound)

          
            return validateLeft and validateRight
           


        return validateBST(root, float("-inf"), float("inf"))

