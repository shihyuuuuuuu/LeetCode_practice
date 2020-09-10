# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root:
            if root.left:
                if root.left.val != root.val:
                    return False
            if root.right:
                if root.right.val != root.val:
                    return False
            l_uni = self.isUnivalTree(root.left)
            r_uni = self.isUnivalTree(root.right)
            return l_uni and r_uni
        return True
