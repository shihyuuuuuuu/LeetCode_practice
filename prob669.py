# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        l = self.trimBST(root.left, low, high)
        r = self.trimBST(root.right, low, high)
        if low <= root.val <= high:
            root.left = l
            root.right = r
            return root
        elif root.val < low:
            return r
        elif root.val > high:
            return l

        # Can also be written like this
        if not root:
            return None
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        elif root.val < low:
            root = root.right
            return self.trimBST(root, low, high)
        elif root.val > high:
            root = root.left
            return self.trimBST(root, low, high)
