# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        candidateNodes = []

        def findStarts(node, sub):
            if not node:
                return

            if node.val == sub.val:
                candidateNodes.append(node)

            findStarts(node.left, sub)
            findStarts(node.right, sub)

        findStarts(root, subRoot)

        def dfs(node1, node2):
            if not node1 and not node2:
                return True

            if (not node1 and node2) or (node1 and not node2):
                return False

            if node1.val != node2.val:
                return False

            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right


        for c in candidateNodes:
            if dfs(subRoot, c):
                return True

        return False

        
            
