# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val

            if not node.right and not node.left:
                return curSum == targetSum

            left = dfs(node.left, curSum)
            right = dfs(node.right, curSum)

            if left or right:
                return True
        
            return False

        return dfs(root, 0)