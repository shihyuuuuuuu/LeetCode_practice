"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if root:
            ans.append(root.val)
            for i in root.children:
                ans += self.preorder(i)
        return ans
