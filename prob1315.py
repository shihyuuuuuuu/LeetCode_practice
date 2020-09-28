# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def DFS(root, elders):
            if not root:
                return
            elders <<= 1
            elders |= 0 if root.val & 1 else 1
            elders &= 0x7
            if elders >> 2:
                self.SUM += root.val
            DFS(root.left, elders)
            DFS(root.right, elders)
        
        self.SUM = 0
        DFS(root, 0)
        return self.SUM
