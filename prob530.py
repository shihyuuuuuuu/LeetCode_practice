# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def DFS(root, arr):
            if not root:
                return arr
            arr = DFS(root.left, arr)
            arr.append(root.val)
            arr = DFS(root.right, arr)
            return arr
        
        arr = DFS(root, [])
        min_diff = float('inf')
        for i in range(len(arr)-1):
            min_diff = min(min_diff, arr[i+1]-arr[i])
        return min_diff
