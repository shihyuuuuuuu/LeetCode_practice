# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []
        def DFS(root, path):
            if not root:
                return
            path += str(root.val) + ' '
            if not root.left and not root.right:
                self.ans.append('->'.join(path.split()))
            DFS(root.left, path)
            DFS(root.right, path)
        DFS(root, "")
        return self.ans
