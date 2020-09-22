# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # Using BFS
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            ans.insert(0, [i.val for i in queue])
            for i in range(len(queue)):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
        return ans
        
        # Using DFS
        def DFS(root, level):
            if not root:
                return
            if len(self.ans) < level:
                self.ans.append([root.val])
            else:
                self.ans[level-1].append(root.val)
            DFS(root.left, level+1)
            DFS(root.right, level+1)
        self.ans = []
        DFS(root, 1)
        return self.ans[::-1]
