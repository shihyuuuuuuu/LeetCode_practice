# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def DFS(root, path):
            if not root:
                path.pop()
                return path
            if root == target:
                path.append(-1)
                return path
            path = DFS(root.left, path+[0])
            path = DFS(root.right, path+[1])
            if path[-1] != -1:
                path.pop()
            return path
        path = DFS(original, [])
        for i in path:
            if i == -1:
                return cloned
            cloned = cloned.right if i else cloned.left
