# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def DFS(root, depth):
            if not root:
                return
            if depth > self.deepest:
                self.deepest = depth
                self.SUM = root.val
            elif depth == self.deepest:
                self.SUM += root.val
            DFS(root.left, depth+1)
            DFS(root.right, depth+1)

        self.SUM, self.deepest = 0, -1
        DFS(root, self.deepest)
        return self.SUM
