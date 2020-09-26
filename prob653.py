# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def DFS(root):
            if not root:
                return
            DFS(root.left)
            sort.append(root.val)
            DFS(root.right)
        
        sort = []
        DFS(root)
        l, r = 0, len(sort)-1
        while l < r:
            s = sort[l] + sort[r]
            if s < k:
                l += 1
            elif s > k:
                r -= 1
            else:
                return True
        return False
