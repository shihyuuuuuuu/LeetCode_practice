# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        def DFS(root, l):
            if not root:
                return
            DFS(root.left, 1)
            DFS(root.right, 0)
            if l and not root.left and not root.right:
                self.ans += root.val
        DFS(root, 0)
        return self.ans
