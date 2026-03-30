# Hsuan Hsuan

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # curr = root
        # while curr:
        #     if p.val < curr.val and q.val < curr.val:
        #         curr = curr.left
        #     elif p.val > curr.val and q.val > curr.val:
        #         curr = curr.right
        #     else:
        #         return curr
        # return
        
        # Recursion
        # if not root:
        #     return
        # if root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # if root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # return root

        # what if the tree is just a Binary Tree
        if root is None or root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
