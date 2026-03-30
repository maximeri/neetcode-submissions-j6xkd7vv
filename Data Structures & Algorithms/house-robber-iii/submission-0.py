# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
       
        def dfs(node):
            if not node:
                return [0, 0]

            # [wNode, woNode]
            leftPairs = dfs(node.left)
            rightPairs = dfs(node.right)
            wNode = node.val + leftPairs[1] + rightPairs[1]
            woNode = max(leftPairs) + max(rightPairs)
            return [wNode, woNode]


        return max(dfs(root))



