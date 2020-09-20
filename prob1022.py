# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.DFS(root, 0, 0)
    
    def DFS(self, root, tmp, ans):
        if not root:
            return ans
        tmp = (tmp << 1) | root.val
        if not root.left and not root.right:
            return ans + tmp
        ans = self.DFS(root.left, tmp, ans)
        ans = self.DFS(root.right, tmp, ans)
        return ans
