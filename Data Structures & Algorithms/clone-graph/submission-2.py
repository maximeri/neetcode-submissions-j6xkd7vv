"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = {} 

        # 1: node1, 2: node2, 3: node3

        # return node
        def dfs(node):
            if node.val in nodes:
                return nodes[node.val]

            copy = Node(node.val)
            nodes[copy.val] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy


        return dfs(node)

        