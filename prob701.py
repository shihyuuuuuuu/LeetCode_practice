# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(root, val):
            if val > root.val:
                if root.right:
                    search(root.right, val)
                else:
                    root.right = TreeNode(val)
            elif val < root.val:
                if root.left:
                    search(root.left, val)
                else:
                    root.left = TreeNode(val)
        if not root:
            return TreeNode(val)
        search(root, val)
        return root
