# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, current: Optional[TreeNode]) -> int:
        if not current:
            return 0

        return 1 + max(self.maxDepth(current.left), self.maxDepth(current.right))