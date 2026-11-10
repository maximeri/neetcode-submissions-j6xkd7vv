# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        ps, qs = [], []
        
        def getPath(node, target, path: list):
            if not node:
                return False
            
            path.append(node)

            if node.val == target.val:
                return True

            if getPath(node.left, target, path):
                return True
           
            if getPath(node.right, target, path):
                return True

            path.pop()

            return False

        getPath(root, p, ps)
        getPath(root, q, qs)

        ans = None
        for pnode in ps:
            for qnode in qs:
                if pnode == qnode:
                    ans = pnode

        return ans
        


        



            