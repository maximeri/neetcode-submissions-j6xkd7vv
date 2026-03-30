class Node:
    def __init__(self, total: int, L: int, R: int):
        self.sum = total
        self.left = None # pointer (left children node)
        self.right = None # pointer (right children node)
        self.L = L # index
        self.R = R # index

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    # O(n)
    def build(self, nums, L, R):
        # leaf node
        if L == R:
            return Node(nums[L], L, R)

        root = Node(0, L, R)
        M = (L + R) // 2 # L + (R - L) // 2 alternativly
        root.left = self.build(nums, L, M) # left subtree
        root.right = self.build(nums, M+1, R) # right subtree
        root.sum = root.left.sum + root.right.sum
        return root
    
    # O(logn)
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val) -> None:
        if root.L == root.R:
            root.sum = val
            return

        M = (root.L + root.R) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum
    
    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, root, L, R):
        if R < root.L or L > root.R:
            return 0
        if L <= root.L and R >= root.R:
            return root.sum
        return self.query_helper(root.left, L, R) + self.query_helper(root.right, L, R)


