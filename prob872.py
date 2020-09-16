# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1, l2 = [], []
        self.DFS(root1, l1)
        self.DFS(root2, l2)
        return l1 == l2
        
    def DFS(self, root: TreeNode, l):
        if not root:
            return
        if not root.left and not root.right:
            l.append(root.val)
            return
        self.DFS(root.left, l)
        self.DFS(root.right, l)
