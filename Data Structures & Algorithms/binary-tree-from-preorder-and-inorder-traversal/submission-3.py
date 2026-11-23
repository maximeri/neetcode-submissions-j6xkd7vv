# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # inorder: left -> root -> right

        preIdx = 0

        # inorder arr to hashmap O(n) => O(1)
        """
        {
            2: 0,
            1: 1,
            3: 2,
            4: 3
        }
        """
        inIdx = {val: i for i, val in enumerate(inorder)}
        # 用 inorder 中 [left, right] 這個範圍的元素建出 subtree，並回傳它的 root。
        
        def build(left: int, right:int) -> TreeNode | None:
            nonlocal preIdx

            if left > right:
                return None

            root = TreeNode(preorder[preIdx])
            rootIdx = inIdx[preorder[preIdx]]
            preIdx += 1

            root.left = build(left, rootIdx - 1)
            root.right = build(rootIdx + 1, right)

            return root


        return build(0, len(inorder) - 1)




        