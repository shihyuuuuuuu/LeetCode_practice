# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            else:
                ans = self.searchBST(root.left, val)
                if ans:
                    return ans
                ans = self.searchBST(root.right, val)
                if ans:
                    return ans
        return None
