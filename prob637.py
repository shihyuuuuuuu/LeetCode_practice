# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = {}
        ans = []
        def level(node, l):
            if l in levels:
                levels[l].append(node.val)
            else:
                levels[l] = [node.val]
            if node.left:
                level(node.left, l+1)
            if node.right:
                level(node.right, l+1)
        level(root, 0)
        for i in range(len(levels)):
            ans += [np.mean(levels[i])]
        return ans        
        
