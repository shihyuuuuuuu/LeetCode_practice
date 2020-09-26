# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Using the feature of BST (Better solution)
        def search(root):
            if root.val > p.val and root.val > q.val:
                return search(root.left)
            elif root.val < p.val and root.val < q.val:
                return search(root.right)
            else:
                return root
        return search(root)
        
        # Solution before I noticed that the tree is a BST
        paths = []
        def DFS(root, path):
            if not root or len(paths) == 2:
                return
            path.append(root)
            if root.val in [p.val, q.val]:
                paths.append(path.copy())
            DFS(root.left, path)
            DFS(root.right, path)
            path.pop()
            return
        DFS(root, [])
        for i in paths[0][::-1]:
            if i in paths[1]:
                return i
