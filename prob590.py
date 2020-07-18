"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if root:
            for i in root.children:
                ans += self.postorder(i)
            ans.append(root.val)
        return ans
