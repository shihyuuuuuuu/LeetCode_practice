# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def traverse(root, path):
            if not root:
                path.append(None)
                return
            path.append(root.val)
            traverse(root.left, path)
            traverse(root.right, path)
        p_path, q_path = [], []
        traverse(p, p_path)
        traverse(q, q_path)
        return p_path == q_path
