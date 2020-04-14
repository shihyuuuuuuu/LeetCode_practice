# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = 0
    def inorder(self, node: TreeNode, L, R):
        if node:
            self.inorder(node.left, L, R)
            if L <= node.val <= R:
                self.ans += node.val
            self.inorder(node.right, L, R)
        
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.inorder(root, L, R)
        return self.ans
