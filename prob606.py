# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def DFS(t):
            if not t:
                return ""
            ret = str(t.val)
            if t.left or t.right:
                ret += '(' + DFS(t.left) + ')'
                if t.right:
                    ret += '(' + DFS(t.right) + ')'
            return ret
        
        return DFS(t)
