# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_depth = 0
    def inorder(self, node, depth):
        if not node: return None
        if depth + 1 > self.max_depth: self.max_depth = depth+1
        self.inorder(node.left, depth+1)
        self.inorder(node.right, depth+1)

    def maxDepth(self, root: TreeNode) -> int:
        self.inorder(root, 0)
        return self.max_depth
