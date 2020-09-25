# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def maxTree(nums):
            if not nums:
                return None
            idx = nums.index(max(nums))
            return TreeNode(nums[idx], maxTree(nums[:idx]), maxTree(nums[idx+1:] if nums[idx] != nums[-1] else []))
        return maxTree(nums)
