# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    new_root = TreeNode()
    curr_node = new_root
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.increasingBST(root.left)
            self.curr_node.right = TreeNode(root.val)
            self.curr_node = self.curr_node.right
            self.increasingBST(root.right)
        return self.new_root.right
